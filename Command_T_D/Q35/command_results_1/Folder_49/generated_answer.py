import re

def remove_repeat_chars(s):
    return re.sub('((?=([^aieou]))\x01)+', '', s[90:-200])