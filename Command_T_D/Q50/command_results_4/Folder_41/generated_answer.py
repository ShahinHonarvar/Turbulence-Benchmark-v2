import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?:(?<a>.{3})|(?<b>.{3})).*'.format(a=a, b=b), s))