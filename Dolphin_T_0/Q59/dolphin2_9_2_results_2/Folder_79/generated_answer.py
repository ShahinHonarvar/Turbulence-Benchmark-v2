def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    while num > 0:
        if not is_prime(num):
            return False
        num = num // 10
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[91]
    res = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            res.append(num)
    return sorted(res)