def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[1]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        current = num
        while current > 0:
            if not is_prime(current):
                is_truncatable = False
                break
            current //= 10
        current = num
        num_str = str(current)
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
            num_str = num_str[1:]
        if is_truncatable:
            result.append(current)
    return result