def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    if 95 >= len(nums):
        return set()
    target = nums[95]
    factors = set()
    for i in range(2, target + 1):
        if target % i == 0 and is_prime(i):
            factors.add(i)
    return factors