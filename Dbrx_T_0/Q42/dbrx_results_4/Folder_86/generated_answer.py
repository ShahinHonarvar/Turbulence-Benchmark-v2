def prime_factors(numbers):
    primes = set()
    for num in numbers[:195]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
                num //= i
                i -= 1
    return primes