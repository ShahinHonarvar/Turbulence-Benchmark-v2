def prime_factors(numbers):

    def primes(n):
        result = set()
        factor = 2
        while factor * factor <= n:
            while n % factor == 0:
                result.add(factor)
                n //= factor
            factor += 1
        if n > 1:
            result.add(n)
        return result
    if len(numbers) <= 10:
        return set()
    return primes(numbers[10])