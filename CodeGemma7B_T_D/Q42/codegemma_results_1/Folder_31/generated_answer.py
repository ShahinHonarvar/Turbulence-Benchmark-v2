def prime_factors(nums):
    return set(filter(lambda x: all((x % d for d in range(2, x))), nums))