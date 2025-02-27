def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[6]
    res = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            t = s
            while t:
                if not is_prime(int(t)):
                    break
                t = t[1:]
            else:
                res.append(i)
    return res