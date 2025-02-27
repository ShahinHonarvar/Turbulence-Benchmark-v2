import re

def remove_repeat_chars(s):
    return re.sub('(\\w){100}(?!\x01){200}(\\w)', '\x01', s)