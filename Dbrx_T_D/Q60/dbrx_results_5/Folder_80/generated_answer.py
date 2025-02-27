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

def truncate_left_right(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    if not is_prime(n % 10 + 1):
        return False
    return truncate_left_right(n // 10)

def all_left_right_truncatable_prime(t):
    x = t[13]
    result = []
    for i in range(2, x + 1):
        if truncate_left_right(i):
            result.append(i)
    return sorted(result, reverse=True)