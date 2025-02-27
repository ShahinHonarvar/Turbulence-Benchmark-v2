import re

def filter_chars(s):
    return re.sub('((?<=.)\\d{5})([a-z])((?=\\.)\\d{5})', '\x02', s)