def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if n < 10:
        return True
    n = str(n)
    return n[1:-1].isdigit() and is_prime(int(n[1:-1])) and is_truncatable(int(n[1:-1]))

def all_left_right_truncatable_prime(t):
    x = t[39]
    primes = [n for n in range(x, 1, -1) if is_prime(n) and is_truncatable(n)]
    return primes