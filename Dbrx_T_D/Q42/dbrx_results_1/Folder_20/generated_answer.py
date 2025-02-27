def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num > 0:
            n = 53
            while n > 1:
                if num % n == 0:
                    primes.add(n)
                    num //= n
                else:
                    n -= 1
    return primes