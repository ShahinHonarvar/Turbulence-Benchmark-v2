def prime_factors(nums):
    return set([factor for n in nums for factor in get_factors(n)]) - {1}

def get_factors(n):
    factors = set()
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            factors.update({x, n // x})
    if n != 1:
        factors.add(n)
    return factors