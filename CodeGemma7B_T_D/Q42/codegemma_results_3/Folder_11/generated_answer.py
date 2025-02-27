def prime_factors(nums):
    target_num = nums[77]
    prime_factors = set()
    for factor in range(2, int(target_num ** 0.5) + 1):
        while target_num % factor == 0:
            prime_factors.add(factor)
            target_num //= factor
    if target_num > 1:
        prime_factors.add(target_num)
    return prime_factors