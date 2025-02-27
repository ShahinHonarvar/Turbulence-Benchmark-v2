def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[57]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [p for p in primes if all((is_prime(int(''.join(filter(str.isdigit, str(p)[i:])))) for i in range(len(str(p)))))]
    return sorted(right_truncatable_primes, reverse=True) or []