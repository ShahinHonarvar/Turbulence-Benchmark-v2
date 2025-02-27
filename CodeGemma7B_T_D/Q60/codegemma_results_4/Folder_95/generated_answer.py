def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if is_prime(i) and str(i).count('0') == 0 and is_truncatable(i):
            result.append(i)
    return result

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def is_truncatable(i):
    str_i = str(i)
    for j in range(1, len(str_i)):
        if not is_prime(int(str_i[j:])):
            return False
        if not is_prime(int(str_i[:-j])):
            return False
    return True