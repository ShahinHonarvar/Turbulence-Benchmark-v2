def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def truncate_right(n):
    while True:
        if is_prime(n):
            yield n
        n //= 10

def all_right_truncatable_prime(x):
    primes = sorted([n for n in range(2, x) if is_prime(n)], reverse=True)
    right_truncatable = [p for p in primes if set(truncate_right(p)) == set((n for n in truncate_right(p)))]
    return right_truncatable