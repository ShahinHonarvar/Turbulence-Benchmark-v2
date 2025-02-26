def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[94]
    result = []
    for num in range(2, x + 1):
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
        str_current = str(current)
        while len(str_current) > 1:
            str_current = str_current[1:]
            current = int(str_current)
            if not is_prime(current):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)