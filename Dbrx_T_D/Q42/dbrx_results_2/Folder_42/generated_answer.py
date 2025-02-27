def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num % 2 == 0:
            primes.add(2)
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                primes.add(i)
                num //= i
        if num > 2:
            primes.add(num)
    return primes.intersection(set(numbers[276]))