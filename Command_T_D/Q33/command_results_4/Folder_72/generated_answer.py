import re

def return_vowels(s):
    res = re.findall('<[aeiou][^>]*>([a-z]*?)<', s)
    return ['<{}>'.format(e) for e in res if e]