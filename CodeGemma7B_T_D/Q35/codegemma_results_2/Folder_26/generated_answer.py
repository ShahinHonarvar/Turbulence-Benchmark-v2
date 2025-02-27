import re

def remove_repeat_chars(text):
    return re.sub('(?<=\\\\w{68})(.)(?=\\\\w{31})', '', text)