import re

def return_nth_smallest_ascii(s):
    res = re.sub('[^A-Z0-9]{%8,65}', '', s)
    return sorted(res)[5]