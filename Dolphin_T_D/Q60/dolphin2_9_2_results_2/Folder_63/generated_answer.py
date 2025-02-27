def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n[:-1])) or not is_prime(int(str_n[1:])):
            return False
        str_n = str_n[:-1]
        str_n = str_n[1:]
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    return [n for n in range(2, x + 1) if is_truncatable(n) and is_prime(n)]