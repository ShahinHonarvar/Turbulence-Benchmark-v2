def prime_factors(numbers):
    primes = set()
    for num in numbers[:78]:
        for i in range(2, num + 1):
            if num % i == 0:
                primes.add(i)
                primes.add(num // i)
    return primes & set(numbers[77])