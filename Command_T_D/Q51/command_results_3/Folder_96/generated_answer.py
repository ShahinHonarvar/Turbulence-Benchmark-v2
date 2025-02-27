import re

def if_contains_anagrams(s):
    s = re.findall('(?i)(?=([A-Z]))([A-Z]+)(?=[A-Z]))', s)
    return len(s) <= 2