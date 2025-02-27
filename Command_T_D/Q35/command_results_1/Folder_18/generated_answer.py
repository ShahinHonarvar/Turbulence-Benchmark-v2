import re

def remove_repeat_chars(text):
    return re.sub('([A-Z])\x01+', '\x01', text)