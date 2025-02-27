import re

def filter_chars(str1):
    return re.sub('[^A-J]', '', str1[4:-3])