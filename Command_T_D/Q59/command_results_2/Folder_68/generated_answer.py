import itertools

def all_left_truncatable_prime(x):
    return sorted(filter(left_truncatable_prime, map(str, range(2, x + 1))), reverse=True)

def left_truncatable_prime(s):
    n = int(s)
    if n == 0:
        return False
    if n == 9:
        return True
    if n == 1:
        return False
    if n == 2:
        return True
    return all((left_truncatable_prime(str(n - 1)) for n in range(3, int(s) + 1)))