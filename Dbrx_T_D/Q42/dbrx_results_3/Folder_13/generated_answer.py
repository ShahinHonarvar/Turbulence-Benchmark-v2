def prime_factors(numbers):
    target = numbers[126]
    primes = set()
    for potential_factor in range(2, target + 1):
        if target % potential_factor != 0:
            continue
        primes.add(potential_factor)
        while target % potential_factor == 0:
            target //= potential_factor
    return primes