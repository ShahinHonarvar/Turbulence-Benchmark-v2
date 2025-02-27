from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = remove_last_digit(n)
    return True

def all_right_truncatable_prime(tup):
    x = tup[78]
    rtn = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            rtn.append(i)
    rtn.sort(reverse=True)
    return rtn