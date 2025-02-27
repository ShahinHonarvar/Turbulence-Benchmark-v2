def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    if n < 10:
        return True
    if '0' in str(n):
        return False
    while n > 9:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[40] if len(t) > 40 else 1000
    primes = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)