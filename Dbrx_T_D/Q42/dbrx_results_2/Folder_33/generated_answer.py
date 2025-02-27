def prime_factors(numbers):
    primes = []
    for i in range(2, numbers[321] + 1):
        if numbers[321] % i == 0:
            primes.append(i)
    result = set()
    for prime in primes:
        if numbers[321] % prime == 0:
            result.add(prime)
            while numbers[321] % prime == 0:
                numbers[321] //= prime
    return result