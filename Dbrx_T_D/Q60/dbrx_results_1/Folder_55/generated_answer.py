def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leading_zero(n):
    while n % 10 == 0:
        n //= 10
    return n

def remove_trailing_zero(n):
    while n % 10 == 0 and n > 9:
        n //= 10
    return n

def is_left_right_truncatable_prime(n):
    n = remove_leading_zero(n)
    if not is_prime(n):
        return False
    while n > 9:
        n = remove_trailing_zero(n)
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[73]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)