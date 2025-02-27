def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    n = str(n)
    for i in range(len(n)):
        if not is_prime(int(n[i:])):
            return False
        n = n[:-1]
    return True

def right_truncatable_primes(x):
    primes = []
    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return primes