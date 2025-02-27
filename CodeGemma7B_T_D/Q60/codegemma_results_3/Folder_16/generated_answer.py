def left_truncatable(n):
    while n > 9:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    if is_prime(n):
        return True
    return False

def right_truncatable(n):
    length = len(str(n))
    while length >= 2:
        n = int(str(n)[:-length + 1])
        length -= 1
        if not is_prime(n):
            return False
    if is_prime(n):
        return True
    return False

def is_prime(n):
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    if n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return False
    return True

def all_left_right_truncatable_prime(n):
    result = []
    for x in range(2, n + 1):
        if left_truncatable(x) and right_truncatable(x):
            result.append(x)
    return sorted(result)