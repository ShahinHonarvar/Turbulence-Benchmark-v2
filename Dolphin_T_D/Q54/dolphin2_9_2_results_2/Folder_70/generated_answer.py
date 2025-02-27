import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[432]
    res = [i for i in range(x - 1, 1, -1) if is_prime(i)]
    res_trunc = [i for i in res if all(is_prime((int(str(i)[:-j]) for j in range(1, len(str(i))))))]
    return res_trunc