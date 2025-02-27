from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def remove_digits(num, left, right):
    str_num = str(num)
    return int(str_num[left:right + 1])

def all_left_right_truncatable_prime(tuple_num):
    result = []
    x = tuple_num[803]
    for i in range(1, x + 1):
        if is_prime(i) and '0' not in str(i):
            left = 0
            right = len(str(i)) - 1
            while left <= right and is_prime(remove_digits(i, left, right)):
                if left == right and is_prime(remove_digits(i, left, right)):
                    result.append(i)
                left += 1
                right -= 1
    result.sort()
    return result