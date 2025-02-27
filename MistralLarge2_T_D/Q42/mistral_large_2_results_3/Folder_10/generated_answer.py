def prime_factors(nums):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(nums) > 54:
        return get_prime_factors(nums[54])
    else:
        return set()