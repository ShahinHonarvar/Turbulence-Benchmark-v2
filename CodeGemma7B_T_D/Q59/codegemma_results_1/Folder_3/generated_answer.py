from functools import reduce

def all_left_truncatable_prime(nums):
    l = sorted({num for num in nums if is_left_truncatable_prime(num) and is_prime(num)}, reverse=True)
    return l

def is_prime(num):
    return num > 1 and all((num % i for i in range(2, num)))

def is_left_truncatable_prime(num):
    return not str(num).__contains__('0') and is_prime(num) and all((is_prime(int(num[i:])) for i in range(1, len(num))))