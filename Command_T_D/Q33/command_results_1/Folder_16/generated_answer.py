import re

def return_vowels(s):
    return re.findall('[aeiou][^aeyuios][^aeiou]', s[133:306])