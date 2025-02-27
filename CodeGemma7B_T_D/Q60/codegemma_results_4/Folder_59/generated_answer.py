def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_left_truncatable_prime(x):
    str_x = str(x)
    for i in range(2, len(str_x)):
        if not is_prime(int(str_x[i:])):
            return False
    return True

def is_right_truncatable_prime(x):
    str_x = str(x)
    while len(str_x) > 1:
        if not is_prime(int(str_x)):
            return False
        str_x = str_x[1:]
    return True

def all_left_right_truncatable_prime(x):
    prime_nums = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            prime_nums.append(i)
    prime_nums.sort(reverse=True)
    return prime_nums