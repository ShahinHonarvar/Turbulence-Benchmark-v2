def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_and_right_truncatable(p):
    s, n = (str(p), len(s))
    for l in range(n):
        if not is_prime(int(s[l:n])):
            return False
        if not is_prime(int(s[:l])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[31]
    prime_list = sorted([p for p in range(2, x + 1) if is_prime(p)])
    return [p for p in prime_list if left_and_right_truncatable(p)]