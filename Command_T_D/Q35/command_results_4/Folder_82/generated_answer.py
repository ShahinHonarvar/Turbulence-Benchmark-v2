import re

def remove_repeat_chars(text):
    return re.sub('(?!<\\d){}(?!>200)([a-z])\x01(?!<\\d)', '\x01', text, flags=re.I)