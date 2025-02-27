import re

def filter_chars(s):
    return re.sub('(^|.*[A-Z])([J-Q].).*([A-Z]|$)', '\x01\x03', s)