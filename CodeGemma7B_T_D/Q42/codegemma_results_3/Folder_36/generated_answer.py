def prime_factors(nums):
    result = set()
    for factor in range(2, nums[990] + 1):
        while nums[990] % factor == 0:
            nums[990] //= factor
            result.add(factor)
    return result