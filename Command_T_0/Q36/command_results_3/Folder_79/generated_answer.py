import re

def filter_chars(s):
    return re.sub('[^!A]{%11,%46}', '', s)