import re

def return_n_smallest_chars(s):
    return sorted(re.findall('[A-Z]{%d}'.format(32), s))