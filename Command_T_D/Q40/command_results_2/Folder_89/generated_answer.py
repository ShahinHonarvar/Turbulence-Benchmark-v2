import re

def return_n_smallest_chars(s):
    re_str = re.sub('[^A-Za-z0-9]', '', s)
    return sorted(re_str)[:55]