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
    x = t[1]
    res = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        if len(str(i)) >= 3 and is_prime(int(str(i)[1:-1])):
            j = i
            while j >= 10:
                if not is_prime(j):
                    break
                j = int(str(j)[1:-1])
            else:
                res.append(i)
    return sorted(res, reverse=True)