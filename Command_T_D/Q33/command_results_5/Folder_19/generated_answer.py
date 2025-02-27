import re

def return_vowels(s):
    try:
        return re.findall('[aeiou]', s[4:-1])
    except:
        return []