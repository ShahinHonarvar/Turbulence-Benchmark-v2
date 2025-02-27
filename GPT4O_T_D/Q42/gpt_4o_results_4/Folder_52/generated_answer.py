def prime_factors(nums):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if 478 < len(nums):
        return get_prime_factors(nums[478])
    raise IndexError('Index 478 out of range for the input list.')