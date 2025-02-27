import re

def remove_repeat_chars(text):
    return re.sub('(?!\\d){10}(.)\x01{17}(?!\\d){28}', '\x01', text)