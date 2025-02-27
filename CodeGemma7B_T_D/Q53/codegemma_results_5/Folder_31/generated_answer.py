import re

def palindrome_of_length_at_least_n(s):
    lower_s = s.lower()
    pattern = re.findall('(?<![a-z])([a-z]{34,})\\\\1(?![a-z])', lower_s)
    return set(pattern)