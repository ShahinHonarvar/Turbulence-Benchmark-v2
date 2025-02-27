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

def right_truncatable_prime(p):
    while p % 10 != 0:
        p = p // 10
        if not is_prime(int(p)):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[29]
    primes = []
    for i in range(1, x):
        if is_prime(i) and right_truncatable_prime(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)