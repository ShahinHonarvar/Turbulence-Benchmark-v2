import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\d{35})\x01(?=\\d{64})).', '', s)