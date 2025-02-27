def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[:len(str_num) - i])):
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[1]
    result = []
    for num in reversed(range(1, x)):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)