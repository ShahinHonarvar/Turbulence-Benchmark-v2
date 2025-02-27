def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primes.add(i)
                primes.add(num // i)
                break
            elif i + 1 == int(num ** 0.5) + 1:
                primes.add(num)
    return primes.intersection(set(numbers[42]))