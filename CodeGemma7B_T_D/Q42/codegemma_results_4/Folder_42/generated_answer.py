def prime_factors(nums):
    pf = set()
    for num in nums:
        if num % nums[276] == 0:
            pf.add(num)
    return pf