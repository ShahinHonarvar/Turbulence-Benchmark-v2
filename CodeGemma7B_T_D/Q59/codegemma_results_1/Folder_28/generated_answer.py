def all_left_truncatable_prime(x):
    left_truncatable_prime = []
    for i in range(1, x):
        if is_prime(i):
            if not contains_zero(i) and is_truncated_prime(i):
                left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def contains_zero(x):
    return '0' in str(x)

def is_truncated_prime(x):
    str_x = str(x)
    for i in range(1, len(str_x)):
        if not is_prime(int(str_x[i:])):
            return False
    return True