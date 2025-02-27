def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    num = nums[56]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors