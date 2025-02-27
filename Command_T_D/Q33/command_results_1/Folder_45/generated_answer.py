import re

def return_vowels(s):
    return re.findall('[aeiou][^a]*[bc]'.lower(), s)