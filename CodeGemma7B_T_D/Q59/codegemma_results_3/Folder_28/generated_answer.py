def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate(n):
    result = []
    for i in range(len(str(n))):
        result.append(int(str(n)[i:]))
    return result

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    for i in truncate(n):
        if not is_prime(i):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[19]
    result = []
    for n in range(x):
        if is_left_truncatable_prime(n):
            result.append(n)
    result.sort()
    return result