import re

def remove_repeat_chars(str1):
    return re.sub('((?<=\\s[0-9])\x01+)(?=\\s[0-9])', '', str1[36:-85])