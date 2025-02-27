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

def all_right_truncatable_prime(t):
    x = t[36]
    ret = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                j //= 10
                if not is_prime(j):
                    break
            else:
                ret.append(i)
    return sorted(ret)