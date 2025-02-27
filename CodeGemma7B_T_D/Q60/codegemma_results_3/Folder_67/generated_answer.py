def all_left_right_truncatable_prime(t):
    x = t[71]
    minval = 10 ** (len(str(x)) - 1)
    maxval = min(99, x)
    a = []
    for i in range(minval, maxval + 1):
        if is_prime(i):
            if is_truncatable(i):
                a.append(i)
    a.sort(reverse=True)
    return a

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    for p in range(5, int(n ** 0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    return True

def is_truncatable(n):
    a = str(n)
    for i in range(1, len(a)):
        s1 = int(a[:i])
        s2 = int(a[i:])
        if not is_prime(s1) or not is_prime(s2):
            return False
    return True