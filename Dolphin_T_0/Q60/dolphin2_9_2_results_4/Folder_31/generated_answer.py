def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[50]
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            while len(s) > 1:
                if not '0' in s:
                    if is_prime(int(s[1:-1])):
                        res.append(i)
                s = s[1:-1]
    return sorted(res, reverse=True)