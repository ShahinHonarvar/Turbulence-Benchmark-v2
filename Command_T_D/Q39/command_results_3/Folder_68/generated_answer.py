import re

def return_n_greatest_chars(s):
    s = re.sub('[^A-Z0-9]+', '', s)
    s = sorted(s)[:89]
    return s