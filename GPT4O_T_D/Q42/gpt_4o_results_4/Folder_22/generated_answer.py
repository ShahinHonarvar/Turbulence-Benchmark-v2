def prime_factors(numbers):

    def generate_primes(n):
        sieve = [True] * (n + 1)
        for start in range(2, int(n ** 0.5) + 1):
            if sieve[start]:
                for i in range(start * start, n + 1, start):
                    sieve[i] = False
        return {num for num in range(2, n + 1) if sieve[num]}

    def find_prime_factors(n):
        primes = generate_primes(n)
        factors = set()
        for prime in primes:
            while n % prime == 0:
                factors.add(prime)
                n //= prime
            if n == 1:
                break
        return factors
    if len(numbers) > 72:
        return find_prime_factors(numbers[72])
    return set()