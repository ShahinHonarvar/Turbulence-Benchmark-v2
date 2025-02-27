def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    s = str(n)
    while s and is_prime(int(s)):
        s = s[1:]
    return not s

def all_left_truncatable_prime(t):
    x = t[23]
    return sorted(filter(left_truncatable_prime, range(2, x)))