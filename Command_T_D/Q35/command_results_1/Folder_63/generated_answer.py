import re

def remove_repeat_chars(s):
    return re.sub('(?i)(?<=\\d{5})(\\d{2})\x01+', '\x01', s)