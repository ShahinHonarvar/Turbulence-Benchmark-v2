def prime_factors(nums):
    factor_set = set()
    prime_factor = nums[2]
    for num in range(2, prime_factor):
        while prime_factor % num == 0:
            factor_set.add(num)
            prime_factor //= num
    return factor_set