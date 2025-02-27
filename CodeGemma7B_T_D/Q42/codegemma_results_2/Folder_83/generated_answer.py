def prime_factors(nums):
    nine5 = nums[95]
    prime_factors_set = set()
    for i in range(2, nine5 + 1):
        while nine5 % i == 0:
            prime_factors_set.add(i)
            nine5 //= i
    return prime_factors_set