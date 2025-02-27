def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncable_prime(n):
    while n > 9:
        if not is_prime(n):
            return False
        n = n // 10
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[36]
    primes = []
    for i in range(2, x + 1):
        if is_truncable_prime(i):
            primes.append(i)
    return sorted(primes)