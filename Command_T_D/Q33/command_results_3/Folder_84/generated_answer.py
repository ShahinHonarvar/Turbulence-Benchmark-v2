import re

def return_vowels(s):
    return re.findall('([^BZIVOWXZJIOU])', s[770:852])