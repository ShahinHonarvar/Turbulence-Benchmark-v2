from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    for i in range(10, n + 1):
        if is_prime(i) and all((int(str(i)[:j]) > 1 and is_prime(int(str(i)[:j])) for j in range(1, len(str(i))))):
            yield i

def all_right_truncatable_prime(t):
    x = t[91]
    return sorted((p for p in right_truncatable_prime(x) if p < x))