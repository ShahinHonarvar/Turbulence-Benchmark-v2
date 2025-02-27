from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def trailing_zeros(n):
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[:-i])):
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[69]
    result = []
    for i in range(x - 1, 1, -1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result