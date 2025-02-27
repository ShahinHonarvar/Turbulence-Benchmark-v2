import re

def if_contains_anagrams(s):
    return not re.findall('(?i)(?<=.)(.*?)(?=.)\x01', ' '.join(s))