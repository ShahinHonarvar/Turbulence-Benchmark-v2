def all_left_right_truncatable_prime(tup):
    result = []
    for i in range(20):
        for j in range(22, tup[i]):
            if is_prime(j) and is_truncatable_prime(j):
                result.append(j)
    result.sort(reverse=True)
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        str_num_left = str_num[:i]
        str_num_right = str_num[i:]
        if not (is_prime(int(str_num_left)) and is_prime(int(str_num_right))):
            return False
    return True