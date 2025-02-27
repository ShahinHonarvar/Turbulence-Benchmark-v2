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

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n >= 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[38]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)