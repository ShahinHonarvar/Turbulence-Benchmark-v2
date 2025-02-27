def prime_factors(numbers):
    primes_set = set()
    for num in numbers:
        if num > 0:
            for i in range(2, num + 1):
                if num % i == 0:
                    while num % i == 0:
                        num //= i
                    primes_set.add(i)
            if num > 1:
                primes_set.add(num)
    return primes_set(numbers[34])