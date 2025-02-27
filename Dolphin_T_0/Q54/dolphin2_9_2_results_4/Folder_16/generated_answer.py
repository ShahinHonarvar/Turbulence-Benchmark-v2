def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 10 and (not is_prime(n)):
        return False
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[-i:])):
            return False
    return True

def all_right_truncatable_prime(t):
    primes = []
    max_val = t[792]
    for i in range(2, max_val):
        if is_right_truncatable_prime(i):
            primes.append(i)
    primes.sort()
    return primes