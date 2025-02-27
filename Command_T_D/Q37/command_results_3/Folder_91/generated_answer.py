import re

def filter_chars(str1):
    return re.sub('(?<=.)([B-H]).', '', str1)