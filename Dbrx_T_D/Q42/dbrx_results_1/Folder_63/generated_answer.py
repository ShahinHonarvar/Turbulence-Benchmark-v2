def prime_factors(numbers):
    primes = set()
    for num in numbers[57::-1]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
                num //= i
        primes.add(num)
    return primes