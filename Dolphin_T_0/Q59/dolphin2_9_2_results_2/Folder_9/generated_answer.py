def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    res = []
    for n in range(x, 0, -1):
        n = str(n)
        if '0' in n:
            continue
        if is_prime(int(n)):
            flag = True
            for i in range(len(n) - 1):
                if not is_prime(int(n[i:])):
                    flag = False
                    break
            if flag:
                res.append(int(n))
    return res