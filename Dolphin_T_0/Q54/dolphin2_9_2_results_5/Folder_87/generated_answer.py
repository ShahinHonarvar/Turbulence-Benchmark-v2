def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    primes = [n for n in range(2, x) if is_prime(n)]

    def is_right_truncatable(p):
        return all((is_prime(int(str(p)[-i:])) for i in range(1, len(str(p)))))
    return sorted([p for p in primes if is_right_truncatable(p)], reverse=True)