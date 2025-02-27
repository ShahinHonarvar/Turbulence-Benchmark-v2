def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(p):
    p_str = str(p)
    for i in range(len(p_str) - 1):
        if not is_prime(int(p_str[:i + 1])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[73]
    res = [int(x) for x in sorted(map(int, str(x))) if is_right_truncatable_prime(x)]
    return res[::-1] if res else []