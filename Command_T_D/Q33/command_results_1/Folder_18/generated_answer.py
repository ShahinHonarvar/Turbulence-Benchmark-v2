import re

def return_vowels(s):
    return re.findall('[A-E][^M-Z]*[X-Z]', s)[::-1]