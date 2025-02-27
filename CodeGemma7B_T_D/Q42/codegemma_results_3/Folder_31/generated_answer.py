def prime_factors(nums):
    target_num = nums[66]
    factors = set()
    for i in range(2, int(target_num ** 0.5) + 1):
        while target_num % i == 0:
            factors.add(i)
            target_num //= i
    if target_num > 1:
        factors.add(target_num)
    return factors