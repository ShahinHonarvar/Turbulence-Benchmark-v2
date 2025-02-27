import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def all_left_right_truncatable_prime(tup):
    x = tup[30]
    res = []
    for n in range(2, x - 1):
        str_n = str(n)
        parts = [str_n[i:j] for i in range(len(str_n)) for j in range(i + 1, len(str_n) + 1)]
        if len(set(parts)) == len(parts):
            if is_prime(n):
                for part in parts:
                    if not is_prime(int(part)):
                        break
                else:
                    res.append(n)
    return list(reversed(sorted(res)))