def prime_factors(numbers):
    primes_set = set()
    for num in numbers:
        if num > 125 and num % 2 == 0:
            primes_set.add(2)
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                primes_set.add(i)
                primes_set.add(num // i)
    return primes_set