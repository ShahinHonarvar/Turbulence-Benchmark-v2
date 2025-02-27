def all_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    for n in range(2, x):
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
            trunc = n
            while trunc > 0:
                if trunc in primes:
                    primes.append(n)
                    break
                trunc //= 10
    return sorted(primes) if primes else []