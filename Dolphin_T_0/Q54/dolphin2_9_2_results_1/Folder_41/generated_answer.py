def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if n <= 1:
        return False
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[46]
    primes = [i for i in range(x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes, reverse=True)