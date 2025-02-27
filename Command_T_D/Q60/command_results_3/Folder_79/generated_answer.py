import re
import heapq

def all_left_right_truncatable_prime(test_list):
    for i in range(91, test_list[0] + 1):
        if is_left_and_right_truncatable_prime(str(i)):
            return [int(i)]
    return []

def is_left_and_right_truncatable_prime(s):
    if any(map(str.isdigit, s)) and s[0] != '0' and (s[-1] != '0') and str(s).isprime():
        return re.sub('0+', '', s) == '1' or re.sub('0+', '', s) == '11'
    return False