def prime_factors(numbers):
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    prime_factors = set()
    for num in numbers:
        if num >= 2:
            for p in primes:
                if num % p == 0:
                    prime_factors.add(p)
                    break
            if num > 97:
                for p in range(100, num + 1):
                    if p % 2 == 0:
                        continue
                    if num % p == 0:
                        prime_factors.add(p)
                        break
    return prime_factors[numbers[632]]