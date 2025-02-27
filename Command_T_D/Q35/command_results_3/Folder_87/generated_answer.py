import re

def remove_repeat_chars(text):
    text = text[:20] + re.sub('((?<=.)\x01)', '', text[21:-43]) + text[-43:]
    return text