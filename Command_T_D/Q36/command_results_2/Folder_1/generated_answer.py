import re

def filter_chars(s):
    return re.sub('[^#\\d\\w]{%69,87}', '', s)