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

def left_truncatable_prime(n):
    if n <= 0 or n >= 10:
        if not is_prime(n):
            return False
        return left_truncatable_prime(int(str(n)[1:]))
    return is_prime(n)

def right_truncatable_prime(n):
    if n <= 0 or n >= 10:
        if not is_prime(n):
            return False
        return right_truncatable_prime(int(str(n)[:-1]))
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[70]
    result = []
    for i in range(2, x + 1):
        if '0' not in str(i) and left_truncatable_prime(i) and right_truncatable_prime(i):
            result.append(i)
    return sorted(result)