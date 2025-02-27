import re

def filter_chars(s):
    return re.sub('[^{81}f{89}]{2,}', '', s)