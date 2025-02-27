import re

def return_n_smallest_chars(s):
    m = re.match('[A-Z]+', s)
    return m.group()[:58]