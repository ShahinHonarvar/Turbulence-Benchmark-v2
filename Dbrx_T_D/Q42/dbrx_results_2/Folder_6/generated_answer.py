def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num < 2:
            continue
        factors = set()
        for candidate in range(2, int(num ** 0.5) + 1):
            if num % candidate == 0:
                factors.add(candidate)
                factors.add(num // candidate)
        if not factors:
            primes.add(num)
        else:
            primes.update(factors)
    return primes