def prime_factors(nums):
    return {factor for num in nums for factor in prime_factors_helper(num)}

def prime_factors_helper(num):
    factor = 2
    factors = set()
    while factor * factor <= num:
        while num % factor == 0:
            factors.add(factor)
            num //= factor
        factor += 1
    if num > 1:
        factors.add(num)
    return factors