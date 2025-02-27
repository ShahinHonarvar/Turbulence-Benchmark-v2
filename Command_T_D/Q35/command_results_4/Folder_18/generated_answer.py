import re

def remove_repeat_chars(s):
    return re.sub('(?i)(?<=56)(\\D+)(?=90)', '', s)