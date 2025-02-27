import re

def remove_repeat_chars(s):
    return re.sub('(?!\\A)[A-Z][a-z]{2}(?!\\Z)', '', s)