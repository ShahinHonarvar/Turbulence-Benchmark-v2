import re

def remove_repeat_chars(str):
    str = re.sub('((?<=50)\x01+(?=92))', '', str)
    return str