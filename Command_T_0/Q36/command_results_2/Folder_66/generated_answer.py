import re

def filter_chars(s):
    return re.sub('[^!}]{39,87}', '', s)