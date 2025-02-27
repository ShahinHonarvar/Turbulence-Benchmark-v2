import re

def remove_repeat_chars(s):
    return re.sub('((?<=90)\x01*(?=97))', '', s)