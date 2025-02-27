import re

def return_vowels(s):
    m = re.search('[aeiou](?=.)', s, flags=re.I)
    return s[m.start():m.end()]