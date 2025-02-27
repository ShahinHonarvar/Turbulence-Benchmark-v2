import re

def if_contains_anagrams(s):
    return re.sub('([a-z]+)(?=([a-z]+)$)', '1', s) in s