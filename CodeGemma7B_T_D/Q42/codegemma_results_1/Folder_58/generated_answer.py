def prime_factors(nums):
    target_index = 714
    prime_factors = set()
    if target_index < len(nums):
        target_number = nums[target_index]
        for factor in range(2, int(target_number ** 0.5) + 1):
            while target_number % factor == 0:
                prime_factors.add(factor)
                target_number //= factor
    return prime_factors