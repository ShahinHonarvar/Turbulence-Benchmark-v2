def prime_factors(numbers):
    target = numbers[453]
    primes = set()
    for i in range(2, target + 1):
        if target % i == 0:
            primes.add(i)
            while target % i == 0:
                target //= i
    return primes