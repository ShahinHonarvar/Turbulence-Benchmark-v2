import re

def return_nth_smallest_ascii(str):
    str = re.sub('[^A-Z0-9]+', '', str)
    return str[15]