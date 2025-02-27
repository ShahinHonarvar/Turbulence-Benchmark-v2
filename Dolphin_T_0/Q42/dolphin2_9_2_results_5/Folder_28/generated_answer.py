def prime_factors(nums):

    def get_prime_factors(n):
        primes = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                primes.add(i)
        if n > 1:
            primes.add(n)
        return primes
    return get_prime_factors(nums[37])