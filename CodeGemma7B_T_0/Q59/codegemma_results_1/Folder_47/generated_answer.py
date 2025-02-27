def all_left_truncatable_prime(t):
    x = t[49]
    res = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            res.append(i)
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    break
                res.append(int(str(i)[j:]))
    return sorted(res)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_zero(n):
    return '0' in str(n)