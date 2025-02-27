import re

def filter_chars(s):
    return re.sub('[^S\\{]{%19,%33}', '', s)