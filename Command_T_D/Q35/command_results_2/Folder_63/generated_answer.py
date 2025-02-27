import re

def remove_repeat_chars(s):
    return re.sub('((?=([^81])))\x01+', '', s)