def prime_factors(numbers):
    primes = set()
    for num in numbers[:61]:
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                primes.add(i)
        if num > 1:
            primes.add(num)
    return primes.difference(set(prime_factors(numbers[:-1])))