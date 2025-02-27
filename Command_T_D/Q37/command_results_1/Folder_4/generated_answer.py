import re

def filter_chars(s):
    return re.sub('((?=S){19}(?<=S){33}(?<!\\\\*))', '', s)