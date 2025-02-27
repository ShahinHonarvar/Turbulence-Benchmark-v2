def prime_factors(nums):
    return {x for x in set(nums[97]) if all((x % d != 0 for d in range(2, x)))}