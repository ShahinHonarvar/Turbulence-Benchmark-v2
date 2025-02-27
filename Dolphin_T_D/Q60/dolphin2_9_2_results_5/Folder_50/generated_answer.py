def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n and n % p != 0:
        p += 2
    return p * p > n

def truncate(n):
    while n > 9:
        b = n % 10
        n //= 10
        if not is_prime(b):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[57]
    primes = [i for i in range(2, x + 1) if is_prime(i) and truncate(i)]
    primes.sort(reverse=True)
    return primes