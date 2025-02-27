import re

def filter_chars(string):
    return re.sub('[^!}]{170,195}', '', string)