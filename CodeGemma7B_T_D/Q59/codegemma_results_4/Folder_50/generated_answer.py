def all_left_truncatable_prime(t):
    x = t[57]
    r = []
    for i in range(2, x):
        if is_prime(i) and all_prime(i):
            r.append(i)
    return sorted(r, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True