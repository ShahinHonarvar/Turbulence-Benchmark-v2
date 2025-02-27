def prime_factors(numbers):
    primes = set()
    for num in numbers[:91:90]:
        while not num % 2:
            primes.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while not num % i:
                primes.add(i)
                num //= i
        if num > 2:
            primes.add(num)
    return primes