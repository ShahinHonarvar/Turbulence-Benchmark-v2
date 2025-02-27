def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[466]
    primes = [i for i in range(x) if is_left_truncatable_prime(i) and is_prime(i)]
    return sorted(primes, reverse=True)