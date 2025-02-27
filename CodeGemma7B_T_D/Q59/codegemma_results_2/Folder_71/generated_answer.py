from functools import reduce
from math import sqrt

def is_prime(num):
    return num > 1 and reduce(lambda prev, curr: prev and curr % num != 0, range(2, int(sqrt(num)) + 1), True) and (num % 2 != 0)

def all_left_truncatable_prime(lim):
    ans = []
    for num in range(2, lim):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            val = num
            for digit in str_num[1:]:
                val = int(str(val) + digit)
                if not is_prime(val):
                    break
            else:
                ans.append(num)
    return sorted(ans, reverse=True)