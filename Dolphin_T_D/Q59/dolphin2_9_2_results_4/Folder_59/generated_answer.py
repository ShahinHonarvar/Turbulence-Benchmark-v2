def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def all_left_truncatable_prime(t):
    x = t[84]
    l = []
    for i in range(x - 1, 1, -1):
        j = i
        while j != 0:
            if is_prime(j):
                j //= 10
            else:
                break
        if j == 0:
            l.append(i)
    return l