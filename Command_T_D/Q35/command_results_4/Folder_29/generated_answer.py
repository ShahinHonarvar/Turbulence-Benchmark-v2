import re

def remove_repeat_chars(s):
    return re.sub('((?<=70)\x02(?=98))', '', s)