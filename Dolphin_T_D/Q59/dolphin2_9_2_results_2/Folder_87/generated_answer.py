def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[39]
    return sorted([i for i in range(x, 0, -1) if is_prime(i) and all((int(str(i)[j:]) for j in range(1, len(str(i)))))])