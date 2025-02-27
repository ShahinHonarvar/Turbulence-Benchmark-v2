def prime_factors(nums):
    factors = set()
    for num in nums:
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                factors.add(factor)
                num //= factor
            factor += 1
        if num > 1:
            factors.add(num)
    return factors