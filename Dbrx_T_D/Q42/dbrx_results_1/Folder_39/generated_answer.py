def prime_factors(numbers):
    primes = set()
    for i in range(len(numbers)):
        num = numbers[i]
        if i == 59:
            while num % 2 == 0:
                primes.add(2)
                num //= 2
            for j in range(3, int(num ** 0.5) + 1, 2):
                while num % j == 0:
                    primes.add(j)
                    num //= j
            if num > 2:
                primes.add(num)
    return primes