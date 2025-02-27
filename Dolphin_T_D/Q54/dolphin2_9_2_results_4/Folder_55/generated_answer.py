def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[-i:])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[73]
    l = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            l.append(i)
    return sorted(l, reverse=True)