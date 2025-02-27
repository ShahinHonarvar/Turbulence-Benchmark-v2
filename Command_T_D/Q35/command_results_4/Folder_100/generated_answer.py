import re

def remove_repeat_chars(s):
    return re.sub('((?:\\d|\\w)@+)', '\\1', s[44:-78])