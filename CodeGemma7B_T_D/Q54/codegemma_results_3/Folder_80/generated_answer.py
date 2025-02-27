from math import sqrt

def all_right_truncatable_prime(n):
    all_right = []
    for i in range(2, n):
        if is_prime(i) and is_right_truncatable(i):
            all_right.append(i)
    all_right.sort(reverse=True)
    return all_right

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    y = n
    check = True
    while y > 0:
        if not is_prime(y):
            check = False
            break
        y = int(str(y)[:-1])
    return check