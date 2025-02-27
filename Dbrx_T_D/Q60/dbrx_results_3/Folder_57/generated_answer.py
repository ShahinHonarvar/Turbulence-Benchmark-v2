def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def is_left_and_right_truncatable(n):
    return is_left_truncatable(n) and is_right_truncatable(n)

def all_left_right_truncatable_prime(t):
    x = 1023456789
    result = []
    for i in range(2, x + 1):
        if is_left_and_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)