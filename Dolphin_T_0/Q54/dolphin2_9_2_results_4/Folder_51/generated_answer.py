def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    n = str(n)
    for _ in range(len(n) - 1):
        if not is_prime(int(n)):
            return False
        n = n[:-1]
    return True

def all_right_truncatable_prime(x):
    primes = [i for i in range(2, int(x)) if is_prime(i) and is_right_truncatable_prime(i)]
    return sorted(primes)