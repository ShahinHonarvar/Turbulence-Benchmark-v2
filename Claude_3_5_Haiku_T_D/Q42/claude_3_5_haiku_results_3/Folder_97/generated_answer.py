def prime_factors(numbers):

    def factors(n):
        primes = set()
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                primes.add(divisor)
                n //= divisor
            divisor += 1
        if n > 1:
            primes.add(n)
        return primes
    return factors(numbers[132])