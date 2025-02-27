def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(p):
    s = str(p)
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[945]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return primes