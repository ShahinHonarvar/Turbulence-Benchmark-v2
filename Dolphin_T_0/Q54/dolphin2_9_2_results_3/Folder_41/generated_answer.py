def all_right_truncatable_prime(t):
    x = t[46]
    primes = []
    for p in range(x, 1, -1):
        if is_prime(p):
            if is_right_truncatable_prime(p):
                primes.append(p)
    return primes

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(p):
    str_p = str(p)
    for i in range(1, len(str_p)):
        if not is_prime(int(str_p[:-i])):
            return False
    return True