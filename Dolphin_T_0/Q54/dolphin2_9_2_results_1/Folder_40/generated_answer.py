def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n, x):
    while n > 1:
        if is_prime(n):
            x = n
            n //= 10
        else:
            return False
    return x <= n

def all_right_truncatable_prime(t):
    x = t[10]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable(p, x)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes