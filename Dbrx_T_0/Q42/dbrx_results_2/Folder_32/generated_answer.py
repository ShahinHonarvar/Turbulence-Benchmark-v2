def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num > 0 and isinstance(num, int):
            while num % 2 == 0:
                primes.add(2)
                num //= 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                while num % i == 0:
                    primes.add(i)
                    num //= i
            if num > 2:
                primes.add(num)
    return primes.pop() if len(primes) == 1 else primes