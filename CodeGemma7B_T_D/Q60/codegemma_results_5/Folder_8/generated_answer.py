from math import sqrt

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and (not str(i).startswith('0')) and is_left_right_truncatable(i):
            prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list

def is_left_right_truncatable(n):
    str_n = str(n)
    length = len(str_n)
    for i in range(1, length):
        if not is_prime(int(str_n[:i])) or not is_prime(int(str_n[i:])):
            return False
    return True