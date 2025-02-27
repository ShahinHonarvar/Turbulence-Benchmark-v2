import re

def if_contains_anagrams(s):
    return bool(re.findall('<(?=([a-z]))(?=[a-z])>.*<(?=([a-z]))(?=[a-z])>', s))