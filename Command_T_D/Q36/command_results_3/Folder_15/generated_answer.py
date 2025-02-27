import re

def filter_chars(s):
    return re.sub('((?<=[b-e])h-j)', '', s)