import re

def return_nth_smallest_ascii(str):
    s = re.sub('[^A-z]', '', str)
    return s[12]