def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    while n > 1:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(n_tuple):
    x = n_tuple[24]
    primes = []
    for i in range(2, x):
        if right_truncatable(i):
            primes.append(i)
    return sorted(primes)