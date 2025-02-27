def all_left_truncatable_prime(t):
    x = t[94]
    left_truncatable_primes = []
    for n in range(2, x):
        if '_is_prime(n)' in left_truncatable_primes:
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)

def _is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

def _is_left_truncatable(n):
    if n < 10 or n % 10 == 0:
        return False
    for i in range(len(str(n)) - 1, 0, -1):
        if not _is_prime(int(str(n)[i:])):
            return False
    return True