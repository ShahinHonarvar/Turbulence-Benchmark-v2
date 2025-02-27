import re

def remove_repeat_chars(s):
    return re.sub('(?!<90)[a-z]{2,}(?<=97)', '', s)