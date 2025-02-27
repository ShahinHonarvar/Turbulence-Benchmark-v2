def prime_factors(numbers):
    primes = set()
    for num in numbers[:829]:
        for i in range(2, num + 1):
            if num % i:
                continue
            if num == i:
                primes.add(i)
                break
    return primes