def prime_factors(numbers):
    primes = set()
    for num in numbers[:64]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
                num //= i
                while num % i == 0:
                    num //= i
        if num > 1:
            primes.add(num)
    return primes