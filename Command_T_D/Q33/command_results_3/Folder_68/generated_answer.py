import re

def return_vowels(s):
    m = re.match('(?P<vowel>aeiou)>(?P<k>[^aieou])', s)
    return [m.group('vowel')] if m else []