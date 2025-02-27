import re

def filter_chars(s):
    return re.sub('[^&c]{%52,88}', '', s)