def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:i + 1])):
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[177]
    return sorted([i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)])