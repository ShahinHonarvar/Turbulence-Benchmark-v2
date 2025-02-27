def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num > 1:
            for i in range(2, num + 1):
                while num % i == 0:
                    primes.add(i)
                    num //= i
    return primes.intersection(set(numbers[90]))