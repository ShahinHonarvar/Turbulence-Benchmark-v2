def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[:i + 1])) or not is_prime(int(str(n)[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[29]
    result = []
    for i in range(10, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)