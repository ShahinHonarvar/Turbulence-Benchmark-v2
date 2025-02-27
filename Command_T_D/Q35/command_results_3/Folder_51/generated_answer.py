import re

def remove_repeat_chars(s):
    return re.sub('(?<=\\d\\d)[a-z]+(?=\\d\\d)', '', s)