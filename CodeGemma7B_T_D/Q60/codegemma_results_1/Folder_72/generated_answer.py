import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[31]
    lst = []
    for n in range(2, x + 1):
        if is_prime(n):
            str_n = str(n)
            if '0' in str_n:
                continue
            for i in range(1, len(str_n)):
                if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                    break
            else:
                lst.append(n)
    return sorted(lst, reverse=True)