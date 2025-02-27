def all_right_truncatable_prime(x):
    x = x[19]
    s = [str(i) for i in range(2, x + 1) if is_prime(i) and is_right_truncatable(i, str(i))]
    return sorted(s) if s else []

def is_prime(n):
    if n <= 3:
        return n == 2 or n == 3
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable(n, s):
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True