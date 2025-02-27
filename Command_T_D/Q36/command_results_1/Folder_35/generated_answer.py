import re

def filter_chars(str1):
    return re.sub('[^A-Z0-9]', '', str1[163:-3])