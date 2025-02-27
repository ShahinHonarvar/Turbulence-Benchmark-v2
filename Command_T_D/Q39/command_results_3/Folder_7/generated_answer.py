import re

def return_n_greatest_chars(s):
    m = re.match('[a-z]+', s)
    s = m.group()
    return s[:49]