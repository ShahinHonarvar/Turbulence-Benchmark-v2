import re

def return_n_greatest_chars(s):
    m = re.match('(\\S+)', s)
    return m.group().split('')[:35]