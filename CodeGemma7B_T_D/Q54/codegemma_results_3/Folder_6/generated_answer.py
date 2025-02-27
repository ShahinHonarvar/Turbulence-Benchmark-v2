def all_right_truncatable_prime(t):
    for i in range(74):
        p = t[i]
        while p >= 10 and is_prime(p):
            p //= 10
        if p == 2 or p == 3:
            if i == 73:
                return [p]
        elif p == 5:
            if i >= 72:
                return [p]
        elif p == 7:
            if i >= 74:
                return [p]
    return []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True