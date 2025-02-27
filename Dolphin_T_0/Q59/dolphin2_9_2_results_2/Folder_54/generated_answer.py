def all_left_truncatable_prime(args):
    x = args[88]
    primes = get_primes_less_than(x)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable(prime):
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def get_primes_less_than(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            for i in range(p ** 2, n, p):
                primes[i] = False
    return [p for p in range(2, n) if primes[p]]

def is_left_truncatable(n):
    if n < 2 or '0' in str(n):
        return False
    while n:
        if not get_primes_less_than(n)[0]:
            return False
        n //= 10
    return True