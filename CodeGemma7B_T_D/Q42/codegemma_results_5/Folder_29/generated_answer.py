from math import sqrt

def prime_factors(nums):
    factorization = set()
    for factor in range(2, int(sqrt(nums[19])) + 1):
        while nums[19] % factor == 0:
            factorization.add(factor)
            nums[19] //= factor
    if nums[19] != 1:
        factorization.add(nums[19])
    return factorization