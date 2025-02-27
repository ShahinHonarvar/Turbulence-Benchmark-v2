def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if truncate_left(i):
            result.append(i)
    return sorted(result, reverse=True)