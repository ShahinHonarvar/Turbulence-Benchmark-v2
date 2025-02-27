import re

def remove_repeat_chars(s):
    return re.sub('(?i)(?<=56).*(?<=88).+', 'X', s)