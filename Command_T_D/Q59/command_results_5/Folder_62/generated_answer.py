import re

def all_left_truncatable_prime(arr):
    return sorted(set(re.findall('[1-9][0-9]*', str(arr[70]))))