from functools import reduce
import math

def len_reducer(acc, element):
    return max(acc, len(str(element)))

def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(n):
    prime_list = []
    for number in range(2, n + 1):
        if not ('0' in str(number) and is_prime(number)):
            continue
        str_number = str(number)
        for k in range(1, len(str_number)):
            if not is_prime(int(str_number[k:])):
                break
            if is_prime(int(str_number[:-k])):
                prime_list.append(number)
    prime_list.sort()
    return prime_list