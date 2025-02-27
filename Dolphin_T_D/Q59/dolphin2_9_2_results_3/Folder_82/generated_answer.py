def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def left_truncatable(n):
    if n <= 1:
        return False
    while n:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[69]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if left_truncatable(i) and is_prime(i):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes