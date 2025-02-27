import re

def return_nth_smallest_ascii(str_):
    str_ = re.sub('[^A-z]', '', str_)
    return str_[12:55].index(min(str_[12:55]))