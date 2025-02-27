def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if n < 2:
        return False
    while n > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    primes = [n for n in range(x) if right_truncatable_prime(n)]
    return sorted(primes, reverse=True)