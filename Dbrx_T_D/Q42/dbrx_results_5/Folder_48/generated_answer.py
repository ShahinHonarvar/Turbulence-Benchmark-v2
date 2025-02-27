def prime_factors(numbers):
    prime_factors = set()
    primes = generate_primes(numbers[247])
    for prime in primes:
        while numbers[247] % prime == 0:
            prime_factors.add(prime)
            numbers[247] //= prime
    return prime_factors

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if sieve[p]:
            primes.append(p)
            for i in range(p ** 2, n + 1, p):
                sieve[i] = False
        p += 1
    for p in range(p, n + 1):
        if sieve[p]:
            primes.append(p)
    return primes