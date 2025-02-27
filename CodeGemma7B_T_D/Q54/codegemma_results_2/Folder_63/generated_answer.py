from math import sqrt

def is_prime(x):
    if x % 2 == 0 or x == 1:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[88]
    result = []
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                result.append(i)
    return sorted(result)