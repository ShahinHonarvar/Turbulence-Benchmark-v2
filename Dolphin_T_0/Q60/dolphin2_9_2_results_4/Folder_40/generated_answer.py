def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_truncatable_prime(p):
    str_p = str(p)
    n = len(str_p)
    for i in range(1, n - 1):
        if str_p[i] == '0':
            return False
        if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:i])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)