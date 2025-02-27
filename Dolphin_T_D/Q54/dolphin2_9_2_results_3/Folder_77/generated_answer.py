def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(p):
    p = str(p)
    while len(p) > 1:
        if not is_prime(int(p)):
            return False
        p = p[:-1]
    return True

def all_right_truncatable_prime(args):
    x = args[767]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and is_right_truncatable(i):
            primes.append(i)
    return primes