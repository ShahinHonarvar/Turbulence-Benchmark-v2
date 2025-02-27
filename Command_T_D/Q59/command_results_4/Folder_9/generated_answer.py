def all_left_truncatable_prime(x):
    primes = []
    num = 2
    while num <= x:
        if all((num % i for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
        num += 1
    return sorted(set(primes))