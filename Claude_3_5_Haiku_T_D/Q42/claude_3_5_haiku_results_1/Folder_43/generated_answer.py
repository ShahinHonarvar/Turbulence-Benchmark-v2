def prime_factors(nums):

    def factors(n):
        primes = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                primes.add(d)
                n //= d
            d += 1
        if n > 1:
            primes.add(n)
        return primes
    return factors(nums[29])