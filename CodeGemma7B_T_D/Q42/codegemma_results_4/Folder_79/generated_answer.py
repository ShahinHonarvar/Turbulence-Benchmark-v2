def prime_factors(nums):
    prime_factors_set = set()
    for num in nums:
        is_prime = True
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime and num in nums[63]:
            prime_factors_set.add(num)
    return prime_factors_set