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

def is_left_truncatable(p):
    str_p = str(p)
    for i in range(len(str_p)):
        if not is_prime(int(str_p[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    if len(t) <= 86:
        return []
    x = t[86]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)