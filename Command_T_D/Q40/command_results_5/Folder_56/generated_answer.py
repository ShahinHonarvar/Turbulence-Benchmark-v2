import re

def return_n_smallest_chars(s):
    s = re.sub('[^A-Z]', '', s)
    return sorted(s)[:21]