import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(arg):
    x = arg[100]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        len_num = len(str_num)
        if '0' in str_num:
            continue
        trunc_left = int(str_num[1:])
        while trunc_left >= 1 and len(str(trunc_left)) < len_num:
            if not is_prime(trunc_left):
                break
            trunc_left = int(str(trunc_left)[1:])
        trunc_right = int(str_num[:-1])
        while trunc_right >= 1 and len(str(trunc_right)) < len_num:
            if not is_prime(trunc_right):
                break
            trunc_right = int(str(trunc_right)[:-1])
        if trunc_left == 1 or trunc_right == 1:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)