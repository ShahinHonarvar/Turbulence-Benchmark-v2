import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?<=\\w)(?=\\w)\x01+\\w+(?=\\w)\x01+', texts))