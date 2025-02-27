def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num < 2:
            continue
        for candidate in range(2, int(num ** 0.5) + 1):
            if num % candidate == 0:
                primes.add(candidate)
                num //= candidate
                while num % candidate == 0:
                    num //= candidate
        if num > 1:
            primes.add(num)
    return primes.intersection(set(numbers[993]))