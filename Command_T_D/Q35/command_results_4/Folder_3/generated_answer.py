import re

def remove_repeat_chars(s):
    return re.sub('(?i)(?=.)\x01+', '', s[56:-2])