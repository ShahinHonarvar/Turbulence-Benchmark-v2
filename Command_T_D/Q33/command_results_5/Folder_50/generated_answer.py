import re

def return_vowels(s):
    re_str = '[aeiouAEIOU][a-w]+'
    return re.findall(re_str, s)