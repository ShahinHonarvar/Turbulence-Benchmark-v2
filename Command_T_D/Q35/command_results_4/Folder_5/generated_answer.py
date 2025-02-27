import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\d)A|B|C|D)(?=\\d)', '', s)