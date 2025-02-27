import re

def all_left_right_truncatable_prime(test_case):
    res = []
    for n in range(10, int(test_case[0]) + 1):
        s = str(n)
        if re.fullmatch('(\\d++){5}\x01', s):
            res.append(int(n))
    return res