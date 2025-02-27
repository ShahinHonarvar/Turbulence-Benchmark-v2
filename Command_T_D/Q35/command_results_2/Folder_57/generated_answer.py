import re

def remove_repeat_chars(s):
    return re.sub('((?:\\d|2[0-4])\\d|2[0-4]\\d|2[0-4][0-9]|[0-9])\x01', '', s[25:-80])