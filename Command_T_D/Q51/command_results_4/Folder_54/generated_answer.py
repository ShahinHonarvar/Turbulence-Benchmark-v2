import re

def if_contains_anagrams(s):
    return not re.findall('(?i)(?<=.)(.*?)(?=.)(.*?)', s)