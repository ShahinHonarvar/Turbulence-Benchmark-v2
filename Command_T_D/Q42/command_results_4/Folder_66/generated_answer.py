def prime_factors(nums):
    nums.sort()
    prime_factors = set()
    for i in range(len(nums)):
        if nums[i] not in prime_factors:
            prime_factors.add(nums[i])
    return prime_factors