def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    if n < 10:
        if is_prime(n):
            return True
        else:
            return False
    elif is_prime(n % 10) and left_truncatable_prime(n // 10):
        return True
    else:
        return False

def all_left_truncatable_prime(t):
    x = t[618]
    result = []
    for i in range(1, x):
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result)