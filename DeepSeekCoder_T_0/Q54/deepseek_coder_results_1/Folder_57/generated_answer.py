def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    while n > 0 and is_prime(n):
        n //= 10
    return n == 0

def all_right_truncatable_prime(t):
    x = t[54]
    primes = [i for i in range(2, x) if right_truncatable_prime(i)]
    return sorted(primes, reverse=True)