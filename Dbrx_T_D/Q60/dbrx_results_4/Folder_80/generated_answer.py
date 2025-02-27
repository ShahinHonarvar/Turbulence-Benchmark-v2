import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    for i in range(1, len(str(n)) + 1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def is_right_truncatable(n):
    for i in range(len(str(n)), 0, -1):
        if not is_prime(int(str(n)[i - 1:])):
            return False
    return True

def left_right_truncatable_prime(x):
    if x < 10:
        return []
    result = []
    for i in itertools.chain(range(10, 100), range(100, x + 1, 10)):
        if is_prime(i) and is_left_truncatable(i) and is_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)