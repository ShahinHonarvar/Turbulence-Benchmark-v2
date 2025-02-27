import re

def remove_repeat_chars(s):
    return re.sub('((?<=86)(?<=89)[a-z]+)', '', s)