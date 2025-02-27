def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(p):
    str_p = str(p)
    for _ in range(len(str_p)):
        if not is_prime(int(str_p)):
            return False
        str_p = str_p[:-1]
        if str_p == '':
            str_p = '2'
    return True

def all_right_truncatable_prime(x):
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])