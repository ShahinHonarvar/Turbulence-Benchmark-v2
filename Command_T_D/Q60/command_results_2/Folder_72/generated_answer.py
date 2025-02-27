import re

def all_left_right_truncatable_prime(x):
    strx = str(x)
    return sorted([x for x in range(2, x) if re.match('[13579][01][23456789]0', str(x))])