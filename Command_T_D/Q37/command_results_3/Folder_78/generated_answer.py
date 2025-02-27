import re

def filter_chars(s):
    return re.sub('(8|9|A|B|C|D|E)', '', s[75:99])