def prime_factors(nums):
    return set(prime_factorize(nums[1]))

def prime_factorize(num):
    factor = 2
    factors = set()
    while factor * factor <= num:
        while num % factor == 0:
            factors.add(factor)
            num //= factor
        factor += 1
    if num != 1:
        factors.add(num)
    return factors