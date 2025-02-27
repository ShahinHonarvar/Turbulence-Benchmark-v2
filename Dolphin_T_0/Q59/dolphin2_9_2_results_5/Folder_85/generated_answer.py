def all_left_truncatable_prime(t):
    x = t[94]
    res = []
    for n in range(2, x):
        n_str = str(n)
        if '0' in n_str:
            continue
        while n_str:
            if not is_prime(int(n_str)):
                break
            n_str = n_str[1:]
        else:
            res.append(n)
    return sorted(res)

def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True