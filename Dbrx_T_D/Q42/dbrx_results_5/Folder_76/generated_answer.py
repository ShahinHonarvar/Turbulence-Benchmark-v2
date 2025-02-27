def prime_factors(numbers):
    primes = set()
    num = numbers[537]
    for i in range(2, num + 1):
        if num % i == 0:
            primes.add(i)
            while num % i == 0:
                num //= i
    return primes