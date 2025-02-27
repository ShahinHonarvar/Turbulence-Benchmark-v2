import math

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(values):
    x = values[0]
    res = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and all((is_prime(int(str(i)[-j:])) for j in range(1, len(str(i))))):
            res.append(i)
    return res