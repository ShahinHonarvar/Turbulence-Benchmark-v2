import re

def remove_repeat_chars(text):
    return re.sub('(?<=.)\x01+', '\\1', text[40:-200])