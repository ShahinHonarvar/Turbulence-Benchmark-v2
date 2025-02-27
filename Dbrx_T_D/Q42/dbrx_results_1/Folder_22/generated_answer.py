def prime_factors(numbers):
    primes = set()
    for num in numbers[:72] + [2, 3, 5, 7]:
        if all((num % i for i in range(2, num))):
            primes.add(num)
    return primes