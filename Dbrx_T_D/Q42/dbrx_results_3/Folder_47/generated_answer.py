def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i:
                continue
            while num % i == 0:
                primes.add(i)
                num //= i
        if num > 1:
            primes.add(num)
    return primes