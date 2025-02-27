import re

def if_contains_anagrams(s):
    return len(re.findall('(?i)(?<=.)(.*?)(?=.)', s)) >= 194