def is_prime(n):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def is_truncatable(n):
    if n < 10:
        return True
    m = n
    while m:
        if m % 10 == 0:
            return False
        m //= 10
    return all((is_prime(n // 10) for n in range(n, 0, -10)))

def all_left_right_truncatable_prime(t):
    x = t[630]
    return [n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)]