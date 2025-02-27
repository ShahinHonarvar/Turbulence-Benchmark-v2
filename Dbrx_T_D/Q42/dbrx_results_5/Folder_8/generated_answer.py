def prime_factors(numbers):
    primes = set()
    for num in numbers[:50]:
        while num % 2 == 0:
            primes.add(2)
            num //= 2
        i = 3
        while i * i <= num:
            while num % i == 0:
                primes.add(i)
                num //= i
            i += 2
        if num > 2:
            primes.add(num)
    return primes