import re

def all_right_truncatable_prime(test_case):
    return re.findall('([2-9])(5[2357]9)', str(test_case[22]))