def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(tpl):
    x = tpl[125]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    ltr_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(ltr_primes, reverse=True)