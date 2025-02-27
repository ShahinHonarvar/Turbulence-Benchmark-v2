import re

def return_vowels(s):
    m = re.search('<[aeiou]>([a-z]*)', s)
    return list(map(str.lower, m.group(1)))