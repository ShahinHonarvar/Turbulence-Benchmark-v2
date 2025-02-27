import re

def return_nth_smallest_ascii(s):
    str1 = re.sub('[^A-Z]', '', s)
    return str1[13]