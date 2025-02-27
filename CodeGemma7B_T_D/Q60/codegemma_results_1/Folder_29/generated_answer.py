import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple):
    list = []
    for i in tuple:
        temp = str(i)
        if temp.count('0') != 0:
            continue
        if is_prime(int(temp)) and is_prime(int(temp[1:])) and is_prime(int(temp[:len(temp) - 1])):
            list.append(int(temp))
    return sorted(list, reverse=True) if len(list) != 0 else []