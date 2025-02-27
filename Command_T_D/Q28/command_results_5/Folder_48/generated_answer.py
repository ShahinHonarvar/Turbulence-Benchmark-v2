import re

def return_nth_smallest_ascii(str):
    return re.search('[a-z]{%d,%d}'.format(37, 59), str).group()