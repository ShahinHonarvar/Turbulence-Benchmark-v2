import re

def filter_chars(str1):
    return re.sub('<([^w]*)>([^<]*)<w>([^>]*)(>)', '\x02', str1)