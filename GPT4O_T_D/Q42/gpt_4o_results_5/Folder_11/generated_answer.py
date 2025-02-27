def prime_factors(numbers):

    def find_prime_factors(n):
        i = 2
        primes = set()
        while i * i <= n:
            while n % i == 0:
                primes.add(i)
                n //= i
            i += 1
        if n > 1:
            primes.add(n)
        return primes
    if len(numbers) < 78:
        return set()
    return find_prime_factors(numbers[77])