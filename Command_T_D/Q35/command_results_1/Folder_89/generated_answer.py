import re

def remove_repeat_chars(s):
    return re.sub('((?<=55)\x01+(?=84))', '', s)