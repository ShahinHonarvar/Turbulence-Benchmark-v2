import re

def palindrome_of_length_n(s):
    s = s.lower()
    return set(re.findall('\\\\b([a-z]{46})\\\\b(?=(\\\\1))[a-z]*', s))