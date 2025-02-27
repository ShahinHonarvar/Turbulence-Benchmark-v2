from math import sqrt

def is_prime(x):
    if x % 2 == 0 and x > 2:
        return False
    i, w = (3, int(sqrt(x)) + 1)
    while i < w:
        if x % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(x):
    ans, a = ([], x)
    while a > 9:
        a, b = divmod(a, 10)
        if b:
            a *= 10
        elif is_prime(a):
            ans.append(a)
        a -= 1
    return sorted(ans)