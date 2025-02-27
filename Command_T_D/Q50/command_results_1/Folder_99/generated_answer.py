import re

def if_contains_anagrams(list_str):
    return bool(re.findall('(?i)(?<=.)(.*?)(?<=.)\x01', *list_str))