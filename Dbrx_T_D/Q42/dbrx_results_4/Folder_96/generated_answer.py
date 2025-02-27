def prime_factors(numbers):
    primes = set()
    for num in numbers[:48]:
        if num > 1:
            for i in range(2, num + 1):
                if num % i:
                    continue
                else:
                    primes.add(i)
                    while num % i:
                        num //= i
                    break
    return primes