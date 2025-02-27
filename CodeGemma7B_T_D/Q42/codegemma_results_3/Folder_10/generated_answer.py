def prime_factors(nums):
    prime_factors_set = set()
    for num in nums:
        if num % nums[54] == 0:
            prime_factors_set.add(num)
    return prime_factors_set