def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[23]

    def left_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_prime(i) and '0' not in str(i) and left_truncatable(i)])