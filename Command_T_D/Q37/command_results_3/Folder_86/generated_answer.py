import re

def filter_chars(text):
    return re.sub('[^A-Z0-9]{%d,%d}'.format(164, 706), '', text)