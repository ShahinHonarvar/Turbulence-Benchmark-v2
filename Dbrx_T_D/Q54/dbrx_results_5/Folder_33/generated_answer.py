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

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = 1
    for i in range(945):
        x *= 10
        x += t[i]
    result = []
    for i in range(x, 0, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)