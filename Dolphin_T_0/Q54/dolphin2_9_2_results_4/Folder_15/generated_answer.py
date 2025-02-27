def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable_prime(n):
    while n != 0:
        if n % 10 == 0 or not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(ix):
    x = ix[6]
    primes = []
    for n in range(2, x - 1):
        if is_prime(n) and is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)