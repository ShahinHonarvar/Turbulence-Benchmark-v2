from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(limit):
    conv = lambda x, y: x * 10 + y
    maximum = max(limit)
    limits = set(limit)
    result = []
    for number in range(maximum + 1):
        forward = list(map(int, str(number)))
        backward = reduce(conv, forward[::-1])
        if backward in limits and is_prime(backward):
            result.append(backward)
    result.sort()
    return result