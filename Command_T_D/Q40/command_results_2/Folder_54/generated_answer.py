import re

def return_n_smallest_chars(s):
    s = re.findall('[A-z]', s)
    s = sorted(s)[-79:]
    return s