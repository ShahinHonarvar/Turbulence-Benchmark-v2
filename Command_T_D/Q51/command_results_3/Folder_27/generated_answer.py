import re

def if_contains_anagrams(texts):
    return len(re.findall('(?i)(?P<str1>[a-z]){2,}(?P<str2>[a-z]){2,}(?P<str3>[a-z]){2,}\x01(?i)(?P<str4>[a-z]){2,}(?P=str2)\x02(?i)(?P=str3)\x03(?i)(?P=str4)\x04\x01\x02\x03\x04', texts)) <= 113