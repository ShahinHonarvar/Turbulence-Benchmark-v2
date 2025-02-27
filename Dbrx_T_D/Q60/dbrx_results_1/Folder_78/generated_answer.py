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
        i += 2
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[23]
    result = []
    for i in range(1, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)