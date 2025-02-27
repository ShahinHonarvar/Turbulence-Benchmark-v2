def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    while n >= 10:
        if not is_prime(n):
            return False
        n = int(n / 10)
        n = int(n % 10)
    return True

def all_left_right_truncatable_prime(t):
    x = t[803]
    result = []
    for i in range(2, x + '001'):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)