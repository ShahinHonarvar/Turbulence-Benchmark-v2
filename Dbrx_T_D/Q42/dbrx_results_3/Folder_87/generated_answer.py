def prime_factors(numbers):
    primes = set()
    for i in numbers[:97]:
        if i < 2:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.add(i)
    return primes