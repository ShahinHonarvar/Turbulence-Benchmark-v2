import re

def return_n_smallest_chars(s):
    x = re.findall('[A-Z]', s)
    return sorted(x[:84])