import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\s|^)[A-z]+\\d){2}((?=\\s|$)[A-z]+\\d)', '', s[40:-200])