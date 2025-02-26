def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[70]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_truncatable = True
        current = num
        while current > 0:
            if not is_prime(current):
                is_truncatable = False
                break
            current //= 10
        if is_truncatable:
            result.append(num)
    return sorted(result)