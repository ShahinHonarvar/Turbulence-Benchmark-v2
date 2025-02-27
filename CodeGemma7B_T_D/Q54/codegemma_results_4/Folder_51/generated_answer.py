def all_right_truncatable_prime(tuple):
    return sorted([x for x in tuple if is_prime(x) and is_truncatable(x)])

def is_prime(x):
    return True

def is_truncatable(x):
    str_x = str(x)
    for i in range(1, len(str_x)):
        if not is_prime(int(str_x[:-i])):
            return False
    return True