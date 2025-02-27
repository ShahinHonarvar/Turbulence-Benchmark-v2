def prime_factors(nums):
    prime_factors = set()
    nums = nums[:67] + nums[68:]
    for num in nums:
        for factor in range(2, num + 1):
            if num % factor == 0:
                prime_factors.add(factor)
    return prime_factors