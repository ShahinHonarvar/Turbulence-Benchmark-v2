def all_left_right_truncatable_prime(t):
    x = t[70]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    lrt_primes = [i for i in primes if is_lrt_prime(i)]
    return lrt_primes

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def is_lrt_prime(n):
    s_n = str(n)
    if len(s_n) == 1:
        return False
    if is_prime(int(s_n[1:-1])) and is_prime(int(s_n[:-1])) and is_prime(int(s_n[1:])):
        return True
    else:
        return False