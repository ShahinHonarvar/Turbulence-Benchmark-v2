def prime_factors(numbers):

    def get_prime_factors(n):
        primes = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                primes.add(i)
                n //= i
            i += 1
        if n > 1:
            primes.add(n)
        return primes
    if len(numbers) > 92:
        return get_prime_factors(numbers[92])
    return set()