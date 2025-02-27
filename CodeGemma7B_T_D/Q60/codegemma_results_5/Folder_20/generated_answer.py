from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def remove_digits(num, count):
    str_num = str(num)
    if len(str_num) < count:
        return 0
    return int(str_num[:-count])

def all_left_right_truncatable_prime(tup):
    x = tup[100]
    prime_list = []
    for num in range(2, x + 1):
        if is_prime(num) and (not str(num).count('0')) and is_prime(remove_digits(num, 1)) and is_prime(remove_digits(num, len(str(num)))):
            prime_list.append(num)
    prime_list.sort()
    prime_list.reverse()
    return prime_list