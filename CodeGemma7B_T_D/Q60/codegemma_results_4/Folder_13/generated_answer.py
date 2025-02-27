import math

def is_prime(n):
    if n <= 1:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, n + 1):
        if is_prime(i) and (not (str(i).startswith('0') or str(i).endswith('0'))):
            truncatable = True
            j = str(i)
            while len(j) > 1:
                j = j[1:]
                if not is_prime(int(j)):
                    truncatable = False
                    break
            if truncatable:
                res.append(i)
    return sorted(res)