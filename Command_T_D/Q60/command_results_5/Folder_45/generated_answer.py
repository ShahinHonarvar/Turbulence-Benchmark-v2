def all_left_right_truncatable_prime(x):
    res = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res

def is_left_right_truncatable_prime(num):
    if str(num).count('0') > 1:
        return False
    if num <= 1:
        return True
    if str(num).count('0') == 1:
        return False
    if str(num).count('0') == 0:
        return True
    return False