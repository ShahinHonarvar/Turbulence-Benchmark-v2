import re

def if_contains_anagrams(str_list):
    return bool(re.findall('(?i)(?P<string>[a-z]+)\x01', str_list))