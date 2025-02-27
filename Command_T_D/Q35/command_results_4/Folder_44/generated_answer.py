import re

def remove_repeat_chars(s):
    return re.sub('((?<= )|(?<=\\A))([a-z]{5})((?=\\ )|(?=\\A))', '\x01', s)