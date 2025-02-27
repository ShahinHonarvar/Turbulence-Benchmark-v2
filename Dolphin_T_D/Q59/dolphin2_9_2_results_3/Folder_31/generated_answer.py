def is_prime(n):
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def left_truncatable(p):
    p_str = str(p)
    for i in range(len(p_str) - 1):
        if is_prime(int(p_str[i:])) == False:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[50]
    res = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and left_truncutable(i):
            res.append(i)
    return res