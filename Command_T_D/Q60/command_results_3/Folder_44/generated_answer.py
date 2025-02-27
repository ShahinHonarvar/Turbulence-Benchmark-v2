import re

def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(tup[0], tup[1] + 1):
        if is_left_right_truncatable_prime(str(i)):
            res.append(i)
    return res

def is_left_right_truncatable_prime(num):
    return bool(re.match('(0|1)\x01+\\d{1,2}+\\d{1,2}+\x01+0\x01+\\d{1,2}+0\x01+1\x01', num))