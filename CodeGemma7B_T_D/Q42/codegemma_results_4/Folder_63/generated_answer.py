def prime_factors(nums):
    factor_set = set()
    nums_prime = nums[57]
    for i in range(2, nums_prime + 1):
        while nums_prime % i == 0:
            factor_set.add(i)
            nums_prime //= i
    return factor_set