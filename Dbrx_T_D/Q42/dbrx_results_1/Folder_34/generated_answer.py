def prime_factors(numbers):
    primes = set()
    for num in numbers[:98]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
                num //= i
                while num % i == 0:
                    num //= i
                break
        if num > 1:
            primes.add(num)
    return primes