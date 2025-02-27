def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if not is_prime(int(str(n)[1:])):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[803]
    primes = []
    for num in range(1, x):
        if left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)