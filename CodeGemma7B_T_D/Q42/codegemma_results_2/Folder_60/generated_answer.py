def prime_factors(nums):
    num = nums[88]
    prime_factors_set = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_factors_set.add(i)
            prime_factors_set.add(num // i)
    return prime_factors_set