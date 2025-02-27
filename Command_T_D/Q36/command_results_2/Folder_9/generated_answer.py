import re

def filter_chars(s):
    return re.sub('[^A-Q]{%50,92}', '', s)