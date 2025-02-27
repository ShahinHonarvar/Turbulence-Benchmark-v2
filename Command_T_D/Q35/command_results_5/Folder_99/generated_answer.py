import re

def remove_repeat_chars(s):
    return re.sub('((?<=450)\x01+)(?<=905)', '', s)