def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    n_str = str(num)
    while n_str and is_prime(int(n_str)):
        n_str = n_str[1:]
    return n_str == ''

def all_left_truncatable_prime(tup):
    x = tup[55]
    res = [num for num in range(2, x) if is_left_truncatable_prime(num) and is_prime(num)]
    return sorted(res)