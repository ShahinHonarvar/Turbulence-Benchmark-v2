import re

def return_n_smallest_chars(s):
    m = re.match('([a-z]+)', s)
    return sorted(m.group())[:64]