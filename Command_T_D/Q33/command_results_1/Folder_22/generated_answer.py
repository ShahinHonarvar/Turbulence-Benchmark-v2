import re

def return_vowels(s):
    return re.findall('[aeiou][^z]', s)[56:-1]