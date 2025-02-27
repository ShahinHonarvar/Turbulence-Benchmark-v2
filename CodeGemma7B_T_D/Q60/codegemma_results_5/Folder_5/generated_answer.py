def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(x):
    if not is_prime(x):
        return False
    str_x = str(x)
    length = len(str_x)
    for i in range(1, length):
        left = int(str_x[i:])
        right = int(str_x[:-i])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return primes