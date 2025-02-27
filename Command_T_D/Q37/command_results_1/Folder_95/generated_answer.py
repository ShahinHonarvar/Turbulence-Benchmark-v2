import re

def filter_chars(s):
    return re.sub('\\A(.*?)\\((l inclusive).*?(\\d+)\\)', '\x01(\x02)\x03', s)