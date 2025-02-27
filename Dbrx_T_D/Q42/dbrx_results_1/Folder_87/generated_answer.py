def prime_factors(numbers):
    primes = set()
    for num in numbers[:97]:
        for i in range(2, num + 1):
            if num % i == 0:
                while num % i == 0:
                    num //= i
                primes.add(i)
        if num > 1:
            primes.add(num)
    return primes