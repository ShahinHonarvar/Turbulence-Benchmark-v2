import re

def remove_repeat_chars(str1):
    return re.sub('((?<=\\d)C)(?=\\d)', '', str1)