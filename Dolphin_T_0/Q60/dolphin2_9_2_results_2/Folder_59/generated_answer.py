def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate(n, ld, rd):
    while is_prime(n):
        if n == ld:
            return n
        n = int(str(n)[1:-1])
    return n

def left_right_truncatable_primes(n):
    primes = []
    if n < 2:
        return primes
    if is_prime(n):
        ld = truncate(int(n * 10 + 4), n, n % 10)
        if ld:
            primes.append(ld)
        rd = truncate(int(n + 40), n % 10, n)
        if rd:
            primes.append(rd)
    return primes + left_right_truncatable_primes(n - 1)

def all_left_right_truncatable_prime(t):
    primes = []
    for i in t:
        for j in left_right_truncatable_primes(i):
            primes.append(j)
    return sorted(primes, reverse=True)