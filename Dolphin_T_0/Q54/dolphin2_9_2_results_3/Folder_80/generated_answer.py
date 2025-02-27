def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    last_digit = n % 10
    if not is_prime(n):
        return False
    return is_right_truncatable(n // 10)

def all_right_truncatable_prime(t):
    x = t[14]
    primes = [i for i in range(x - 1, 1, -1) if is_prime(i) and is_right_truncatable(i)]
    return primes if primes else []