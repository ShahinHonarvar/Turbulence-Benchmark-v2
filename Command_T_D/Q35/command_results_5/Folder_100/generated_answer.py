import re

def remove_repeat_chars(str1):
    return re.sub('((?<=\\d)D|(?!\\d\x01)D)', '', str1[44:-78])