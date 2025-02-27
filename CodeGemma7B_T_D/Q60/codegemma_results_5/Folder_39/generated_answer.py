def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def truncate_left_right(x):
    result = []
    for i in range(1, len(str(x))):
        if int(str(x)[i:]) % 2 == 0 or int(str(x)[:i]) % 2 == 0:
            continue
        if is_prime(int(str(x)[i:])):
            if is_prime(int(str(x)[:i])):
                result.append(x)
    return result

def all_left_right_truncatable_prime(p):
    x = p[30]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            if len(str(i)) > 2 and 0 not in str(i):
                if i in truncate_left_right(i):
                    result.append(i)
    return sorted(result, reverse=True)