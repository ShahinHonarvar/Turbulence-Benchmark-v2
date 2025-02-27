def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(vals):
    x = vals[630]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable = [i for i in primes if str(i)[::-1].lstrip('0') in primes]
    return sorted(truncatable, reverse=True) or []