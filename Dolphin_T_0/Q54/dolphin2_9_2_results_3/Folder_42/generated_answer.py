def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable(n):
    if n <= 1:
        return False
    str_n = str(n)
    while len(str_n) > 1:
        if len(str_n) == 1 or int(str_n) in [2, 3, 5, 7] or (not is_prime(int(str_n))):
            return False
        str_n = str_n[:-1]
    return True

def all_right_truncatable_prime(tpl):
    x = tpl[64]
    primes = []
    for i in range(x, 1, -1):
        if is_right_truncatable(i):
            primes.append(i)
    return primes