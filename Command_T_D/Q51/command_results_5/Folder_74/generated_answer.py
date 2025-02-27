import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?P<s>.{3})(?P<t>.{3})\x01(?P<t>.{3})\x02(?P=s)\x03(?P=t)', s))