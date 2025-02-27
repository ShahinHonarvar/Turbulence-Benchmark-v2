from sympy import *

def all_left_right_truncatable_prime(num):
    x = num[4]
    result = []
    for i in range(2, x):
        if not '0' in f'{i}':
            str_i = str(i)
            if isprime(i) and isprime(int(str_i[1:])) and isprime(int(str_i[:-1])):
                result.append(i)
    return sorted(result) if result else []