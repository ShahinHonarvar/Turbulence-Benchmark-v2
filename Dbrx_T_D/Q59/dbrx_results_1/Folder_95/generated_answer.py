def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = int(str(n)[1:])
        if is_prime(n):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[77]
    result = []
    for i in range(1, x):
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result)