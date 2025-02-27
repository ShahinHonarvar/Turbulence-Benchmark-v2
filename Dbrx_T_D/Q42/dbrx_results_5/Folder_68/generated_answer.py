def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num > 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    primes.add(i)
                    break
    return primes.intersection(set(range(numbers[3], 1, -1)))