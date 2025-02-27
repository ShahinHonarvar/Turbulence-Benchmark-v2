import re

def remove_repeat_chars(str):
    return re.sub('((?:\\d|.)){103}(?:\\d|.){802}', '\x01', str)