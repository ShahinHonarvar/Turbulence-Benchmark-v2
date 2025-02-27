def prime_factors(numbers):
    primes = set()
    n = numbers[7]
    i = 2
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes.add(i)
    return primes