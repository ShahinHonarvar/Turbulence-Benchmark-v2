def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:]) if str(n)[1:] else 0
    return True

def all_left_truncatable_prime(tup):
    x = tup[74]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and left_truncatable_prime(i):
            result.append(i)
    return result