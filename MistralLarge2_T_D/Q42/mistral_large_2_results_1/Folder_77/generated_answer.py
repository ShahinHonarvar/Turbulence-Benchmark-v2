def prime_factors(nums):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.add(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(nums) > 985:
        return get_prime_factors(nums[985])
    return set()