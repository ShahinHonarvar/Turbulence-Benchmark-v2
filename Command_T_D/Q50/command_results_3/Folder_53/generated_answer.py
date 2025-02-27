import re

def if_contains_anagrams(s):
    return len(re.findall('\\A(?!\\d)\\w+\x01+', ''.join(s))) >= 11