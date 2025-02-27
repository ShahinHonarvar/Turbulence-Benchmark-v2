import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    i = n
    while i > 0:
        if not is_prime(i):
            return False
        i //= 10
    return True

def all_right_truncatable_prime(params):
    x = params[100]
    lst = [i for i in range(1, x) if is_right_truncatable_prime(i)]
    lst.sort(reverse=True)
    return lst