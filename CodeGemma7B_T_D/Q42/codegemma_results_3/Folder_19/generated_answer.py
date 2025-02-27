def prime_factors(nums):
    prime_factors_set = set()
    for i in range(2, nums[13] + 1):
        while nums[13] % i == 0:
            prime_factors_set.add(i)
            nums[13] //= i
    return prime_factors_set