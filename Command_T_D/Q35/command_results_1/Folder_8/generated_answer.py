import re

def remove_repeat_chars(s):
    return re.sub('(?!^).*(?<=.45).*(?=.48).*(?!\x01).*$', '', s)