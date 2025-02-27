def prime_factors(numbers):
    primes = set()
    for num in numbers[:993]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
    for prime in primes:
        if numbers[993] % prime == 0:
            primes.remove(prime)
    return primes