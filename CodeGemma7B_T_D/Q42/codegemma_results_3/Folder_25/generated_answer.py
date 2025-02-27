def prime_factors(nums):
    factor_set = set()
    num = nums[90]
    for i in range(2, int(num ** 0.5) + 1):
        factor = 0
        while num % i == 0:
            factor += 1
            factor_set.add(i)
            num //= i
    return factor_set