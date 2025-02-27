def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[54]
    res = []
    for i in range(2, x):
        while is_prime(i):
            res.append(i)
            i = int(i / 10)
    return sorted(res)