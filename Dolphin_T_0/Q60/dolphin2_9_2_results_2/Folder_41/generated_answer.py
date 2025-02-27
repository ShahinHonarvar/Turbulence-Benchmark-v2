def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[46]
    res = [i for i in range(2, x + 1) if str(i).count('0') == 0]
    for i in range(10, 0, -1):
        for j in range(9):
            i = 10 * i + j
            if i > x:
                return [n for n in res if is_prime(n)]
            if is_prime(i) and i in res:
                res.append(i)
    return [n for n in res if is_prime(n)]