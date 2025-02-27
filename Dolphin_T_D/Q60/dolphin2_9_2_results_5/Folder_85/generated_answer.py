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

def all_left_right_truncatable_prime(t):
    x = t[94]
    res = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        n = i
        while len(str(n)) > 1:
            n = n // 10
            if not is_prime(n):
                break
        if len(str(n)) >= 2:
            continue
        n = i
        while len(str(n)) > 1:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                break
        if len(str(n)) >= 2:
            continue
        res.append(i)
    return sorted(res)