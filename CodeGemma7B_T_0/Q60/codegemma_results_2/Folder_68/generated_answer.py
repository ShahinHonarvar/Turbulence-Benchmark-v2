def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10 or '0' in str(n):
        return False
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[1]
    result = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result