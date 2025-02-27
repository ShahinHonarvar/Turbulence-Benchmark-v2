def prime_factors(nums):
    return set(factorize(nums[19]))

def factorize(n):
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
    return factors