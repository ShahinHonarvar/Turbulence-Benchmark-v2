import re

def remove_repeat_chars(s):
    return re.sub('(?<=43)\\w+\\w+\\w+\\w+(?<=70)', '', s)