def all_right_truncatable_prime(nums):
    x = nums[50]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            if right_truncatable(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = n ** 0.5
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    if n < 10:
        return True
    while n > 1:
        n = n // 10
        if n == 0:
            return False
        if not is_prime(n):
            return False
    return True