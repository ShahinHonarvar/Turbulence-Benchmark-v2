def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_truncatable(n):
    if n < 10:
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n) - 2):
        if not is_prime(int(str_n[i + 1:])) or not is_prime(int(str_n[:i + 1])) or (not is_prime(int(str_n[i:i + 2]))):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[126]
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)], reverse=True)