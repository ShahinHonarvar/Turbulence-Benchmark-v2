def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[38]
    res = []
    for i in range(2, x):
        if '0' in str(i) or not is_prime(i):
            continue
        if all((is_prime(int(str(i)[n:])) for n in range(1, len(str(i))))):
            res.append(i)
    return sorted(res, reverse=True)