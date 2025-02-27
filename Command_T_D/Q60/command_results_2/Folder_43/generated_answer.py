import re

def all_left_right_truncatable_prime(x_range):
    return [n for n in range(3, x_range[0] + 1) if re.fullmatch('^[13579](?=\\d\x01)86[24568]99', str(n))]