import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = math.sqrt(n) + 1
    for divisor in range(3, int(sqr), 2):
        if n % divisor == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[77]
    res = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                is_truncatable = True
                for j in range(len(str_i) - 1, 0, -1):
                    if not is_prime(int(str_i[j:])):
                        is_truncatable = False
                        break
                if is_truncatable:
                    res.append(i)
    return sorted(res, reverse=True)