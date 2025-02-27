from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[93]
    result = []
    for n in range(2, x):
        if is_prime(n):
            str_n = str(n)
            for i in range(1, len(str_n)):
                if not is_prime(int(str_n[:len(str_n) - i])):
                    break
            else:
                result.append(n)
    return sorted(result)