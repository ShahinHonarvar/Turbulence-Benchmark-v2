def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[945]
    result = []
    for number in range(1, x + 1):
        if is_prime(number) and is_left_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)