import re

def filter_chars(str1):
    return re.sub('([^E~])\\d+([^E~])', '\x01\x02', str1)