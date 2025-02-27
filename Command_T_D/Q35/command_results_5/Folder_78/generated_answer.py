import re

def remove_repeat_chars(s):
    return re.sub('[a-zA-Z0-9]{62,96}', '', s)