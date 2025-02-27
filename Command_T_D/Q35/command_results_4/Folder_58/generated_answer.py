import re

def remove_repeat_chars(s):
    return re.sub('(?!\\A)'.join(re.findall('([^<]+)', s[103:-2])), '', s)