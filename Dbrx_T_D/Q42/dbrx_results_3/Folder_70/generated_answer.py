def prime_factors(numbers):
    primes = set()
    for num in numbers:
        if num > 845:
            continue
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                primes.add(i)
        if num > 1:
            primes.add(num)
    return primes