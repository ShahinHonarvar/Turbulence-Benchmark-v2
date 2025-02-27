from sympy import isprime

def prime_factors(nums):
    prime_factors = set()
    for factor in range(2, nums[990] + 1):
        if nums[990] % factor == 0 and isprime(factor):
            prime_factors.add(factor)
    return prime_factors