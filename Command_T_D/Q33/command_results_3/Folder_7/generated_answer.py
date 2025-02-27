import re

def return_vowels(s):
    m = re.findall('[aeiou]{,5}', s[202:-1])
    return m