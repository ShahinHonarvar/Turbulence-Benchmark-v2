import re

def if_contains_anagrams(s):
    return not re.findall('\\A[a-z]{3}((?=([a-z]){3}){2})', ''.join(s).lower())