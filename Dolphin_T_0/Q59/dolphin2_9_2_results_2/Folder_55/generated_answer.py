def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(number):
    if not is_prime(number):
        return False
    nnumber = number
    while nnumber:
        if not is_prime(nnumber):
            return False
        nnumber //= 10
    return True

def all_left_truncatable_prime(x):
    result = []
    for i in range(x - 1, 1, -1):
        if left_truncatable_prime(i):
            result.append(i)
    return result