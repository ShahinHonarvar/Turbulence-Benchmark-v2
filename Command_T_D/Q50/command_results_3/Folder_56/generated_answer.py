import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?P<a>.*?)(?P<b>.*?)\x01', texts))