def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_trunc(p):
    s = str(p)
    for i in range(len(s) - 1, 0, -1):
        if not is_prime(int(s[i:] + s[:i])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[55]
    l = [i for i in range(x, 1, -1) if is_prime(i) and is_trunc(i)]
    return l