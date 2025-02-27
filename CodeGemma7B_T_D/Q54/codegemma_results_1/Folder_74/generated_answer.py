def all_right_truncatable_prime(tup):
    x = tup[36]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = []
    for p in primes:
        if all((is_prime(int(str(p)[:-i])) for i in range(1, len(str(p))))):
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True