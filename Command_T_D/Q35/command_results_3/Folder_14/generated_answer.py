import re

def remove_repeat_chars(str1):
    str1 = str(re.sub('((?<=\\d)r(?=\\d))', '', str1))
    str1 = str(re.sub('((?<=\\d)s(?=\\d))', '', str1))
    str1 = str(re.sub('((?<=\\d)t(?=\\d))', '', str1))
    return str1