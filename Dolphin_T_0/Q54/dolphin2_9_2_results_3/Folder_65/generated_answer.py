def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    else:
        return is_prime(n) and is_right_truncatable(n // 10)

def all_right_truncatable_prime(t):
    x = t[32]
    primes = [n for n in range(1, x) if is_right_truncatable(n)]
    return sorted(primes)