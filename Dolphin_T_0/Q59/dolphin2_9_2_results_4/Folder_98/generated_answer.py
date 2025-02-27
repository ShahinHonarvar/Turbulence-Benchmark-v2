def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[8]
    res = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            if '0' in s:
                continue
            for j in range(len(s) - 1):
                if not is_prime(int(s[j:])):
                    break
            else:
                res.append(i)
    return res[::-1]