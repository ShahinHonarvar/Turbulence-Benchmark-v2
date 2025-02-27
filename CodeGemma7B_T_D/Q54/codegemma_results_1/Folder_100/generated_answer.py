def all_right_truncatable_prime(t):
    x = t[26]
    out = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            out.append(i)
    return sorted(out)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[:i])):
            return False
    return True