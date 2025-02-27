import re

def return_vowels(s):
    if re.search('[AEIOU](?!F)[^ghH]', s):
        return re.findall('[AEIOU](?!F)[^ghH]', s)
    else:
        return []