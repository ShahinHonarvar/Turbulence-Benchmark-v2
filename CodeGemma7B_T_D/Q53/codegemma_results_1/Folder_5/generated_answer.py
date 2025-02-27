import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    patt = '(?<![a-z])(?<![a-z])([a-z]{46,})\\\\2\\\\1'
    return set(re.findall(patt, s))