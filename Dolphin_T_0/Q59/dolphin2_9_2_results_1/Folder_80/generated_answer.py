def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    n = str(n)
    if '0' in n:
        return False
    for i in range(len(n) - 1, 0, -1):
        if not is_prime(int(n[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    _, x = t
    primes = [i for i in range(x, 1, -1) if is_prime(i) and is_truncatable(i)]
    return primes