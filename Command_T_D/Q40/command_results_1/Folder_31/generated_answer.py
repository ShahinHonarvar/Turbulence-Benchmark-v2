import re

def return_n_smallest_chars(s):
    s = re.sub('[^A-z]', '', s)
    return sorted(s)[-70:]