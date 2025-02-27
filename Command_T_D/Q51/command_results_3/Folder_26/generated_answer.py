import re

def if_contains_anagrams(s):
    return len(re.findall('(?i)(?<=.)(.*?)(?=.)\x01', s)) <= 35