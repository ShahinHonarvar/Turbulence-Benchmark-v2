import re

def return_vowels(s):
    return [c for c in range(50, 51) if re.search('[aeiou]', s[c:v])]