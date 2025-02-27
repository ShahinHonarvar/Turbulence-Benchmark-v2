def prime_factors(numbers):

    def primes(n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    return primes(numbers[410]) if len(numbers) > 410 else set()