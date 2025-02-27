import re

def all_left_right_truncatable_prime(nums):
    return sorted(list(filter(lambda x: left_re.sub('\x01', str(x), x) in right_re.sub('\x01', str(x), x), nums)))