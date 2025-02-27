import re

def return_n_smallest_chars(str_arg):
    str_arg = re.sub('[^A-Z0-9]', '', str_arg)
    str_arg = sorted(str_arg)
    return str_arg[:49]