def is_prime(n):
    if n is None:
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    v = 3
    while v * v <= n:
        if n % v == 0:
            return False
        v += 2
    return True

def all_left_truncatable_prime(t):

    def left_truncatable_prime(n):
        if n == 0:
            return False
        if n < 10:
            return is_prime(n)
        return is_prime(n) and left_truncatable_prime(n // 10)
    x = t[46]
    res = [i for i in range(x - 1, 1, -1) if left_truncatable_prime(i)]
    return res