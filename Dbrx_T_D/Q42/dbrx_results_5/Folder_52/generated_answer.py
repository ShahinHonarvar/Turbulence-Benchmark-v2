def prime_factors(numbers):
    primes = set()
    for num in numbers[:479]:
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                primes.add(i)
        if num > 1:
            primes.add(num)
    return primes.intersection(set(numbers[478]))