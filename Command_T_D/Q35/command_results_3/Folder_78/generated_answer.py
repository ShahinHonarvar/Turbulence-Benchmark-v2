import re

def remove_repeat_chars(s):
    return re.sub('((?<=.)\x02(?=\\.)\x02)+', '', s, flags=re.I)