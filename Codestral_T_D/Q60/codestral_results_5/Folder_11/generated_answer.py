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

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        str_n = str_n[1:]
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
        if not is_prime(int(str_n)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[86]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])