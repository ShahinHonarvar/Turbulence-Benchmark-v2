def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    if n < 10 and (not is_prime(n)):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[:i + 1])):
            return False
    return True

def all_left_truncatable_prime(limit):
    primes = []
    for i in range(2, limit):
        if left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)