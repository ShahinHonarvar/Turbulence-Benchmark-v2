def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[630]
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = [n for n in primes if all((int(str(n)[:-i]) in primes for i in range(1, len(str(n)))))]
    return sorted(right_truncatable_primes, reverse=True) or []