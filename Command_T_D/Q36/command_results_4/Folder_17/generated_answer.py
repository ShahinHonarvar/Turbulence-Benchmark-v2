import re

def filter_chars(s):
    return re.sub('((?<=18)[^K-a]{1,26}(?=95))', '', s)