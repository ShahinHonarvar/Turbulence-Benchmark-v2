def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[20]
    primes = [i for i in reversed(range(2, x + 1)) if is_prime(i)]
    trunc_primes = [i for i in primes if '0' not in str(i) and all((is_prime(int(str(i)[1:-1])) for i in primes))]
    return trunc_primes