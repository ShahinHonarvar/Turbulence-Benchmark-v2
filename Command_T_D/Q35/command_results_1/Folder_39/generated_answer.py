import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\d))\\d+(?=\\d)', ' \x01 \x02', s[44:-91])