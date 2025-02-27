import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(tuple):
    x = tuple[77]
    prime_list = []
    for num in range(2, x):
        if is_prime(num) and left_truncatable(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)