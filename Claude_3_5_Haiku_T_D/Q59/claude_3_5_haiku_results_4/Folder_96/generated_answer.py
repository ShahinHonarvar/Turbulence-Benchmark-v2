def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[29]
    result = []
    for num in range(2, x):
        if is_prime(num) and left_truncatable(num):
            result.append(num)
    return sorted(result)

def left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True