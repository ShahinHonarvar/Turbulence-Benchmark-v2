import re

def remove_repeat_chars(s):
    return re.sub('([a-z]){20}([a-z]){35}(?!\x01)', '\x02', s)