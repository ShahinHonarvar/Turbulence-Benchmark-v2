import re

def all_right_truncatable_prime(n):
    x = n[24]
    return sorted([int(i) for i in re.findall('(2[0-4]9)[0-9]0', str(x))])