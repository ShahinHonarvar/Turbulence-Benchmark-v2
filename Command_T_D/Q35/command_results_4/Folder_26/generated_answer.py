import re

def remove_repeat_chars(s):
    return re.sub('[a-z]{2,}(?=([a-z]{0,68}|([a-z]{0,99})))', '', s)