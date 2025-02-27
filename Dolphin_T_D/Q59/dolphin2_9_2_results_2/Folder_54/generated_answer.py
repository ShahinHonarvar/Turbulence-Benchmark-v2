def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[88]
    l = []
    for i in range(x):
        s = str(i)
        if '0' not in s and is_prime(i):
            ff = s
            while ff and is_prime(int(ff)):
                if len(ff) > 1 and is_prime(int(ff[1:])):
                    ff = ff[1:]
                else:
                    break
            if not ff:
                l.append(i)
    return sorted(l, reverse=True)