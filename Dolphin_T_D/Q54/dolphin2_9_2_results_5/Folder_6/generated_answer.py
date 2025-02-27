def right_truncatable(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[74]
    primes = [n for n in range(2, x) if is_prime(n) and right_truncatable(n)]
    return sorted(primes)