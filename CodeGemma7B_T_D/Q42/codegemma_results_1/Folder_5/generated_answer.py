def prime_factors(nums):
    prime_factor = set()
    for item in nums:
        if item == nums[67]:
            for factor in range(2, int(nums[67] ** 0.5) + 1):
                if nums[67] % factor == 0:
                    prime_factor.add(factor)
                    while nums[67] % factor == 0:
                        nums[67] //= factor
    return prime_factor