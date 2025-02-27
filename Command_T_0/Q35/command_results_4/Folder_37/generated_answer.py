import re

def remove_repeat_chars(s):
    return re.sub('(.)\\1(.)\\1(.)\\1(.)\\1(.)\\1(.)\\1', '\\1\\2\\3\\4\\5\\6\\7', s)