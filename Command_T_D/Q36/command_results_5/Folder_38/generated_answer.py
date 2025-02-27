import re

def filter_chars(string):
    return re.sub('(?<=\\d)[>+<l]+', '', string)