def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n = int(n)
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[767]
    left_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_truncatable_prime(i) and i < 10:
            left_truncatable_primes.append(i)
    return left_truncatable_primes