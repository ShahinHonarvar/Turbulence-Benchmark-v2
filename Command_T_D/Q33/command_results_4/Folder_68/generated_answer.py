import re

def return_vowels(s):
    return re.findall('([^]{{1}}[aeiou][^]{{9}})', s)