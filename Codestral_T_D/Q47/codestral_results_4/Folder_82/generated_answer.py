import re

def palindromes_of_specific_lengths(s):
    s = s[3:301]
    s = re.findall('\\\\b[A-Za-z]{30,301}\\\\b', s)
    s = set(filter(lambda x: x.lower() == x.lower()[::-1], s))
    return s