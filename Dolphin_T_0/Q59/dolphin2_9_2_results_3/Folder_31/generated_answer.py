def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[50]
    primes = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_primes = []
    for p in primes:
        if all(is_prime((''.join(filter(None, str(p)[i:])) for i in range(len(str(p)))))):
            left_truncatable_primes.append(p)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes