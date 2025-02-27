import re

def all_right_truncatable_prime(x):
    return sorted(filter(lambda x: x < x[97] and re.match('(\\d)\\d\x01+$', str(x)), x), key=lambda x: -x)