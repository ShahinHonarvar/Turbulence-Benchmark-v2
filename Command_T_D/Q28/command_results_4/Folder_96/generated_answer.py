import re

def return_nth_smallest_ascii(s):
    r = re.sub('[^A-Z]', '', s)
    return next(sorted(r)[17])