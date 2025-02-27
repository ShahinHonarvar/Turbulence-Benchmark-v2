def prime_factors(numbers):
    primes = set()
    for num in numbers[:985]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
                num = num // i
                i -= 1
    return primes