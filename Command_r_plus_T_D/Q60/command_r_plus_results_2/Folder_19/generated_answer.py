def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[:i] + str_num[i + 1:])) or not is_prime(int(str_num[:i] + str_num[i + 2:])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    result = []
    for num in tup:
        if num > 73:
            break
        if left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)