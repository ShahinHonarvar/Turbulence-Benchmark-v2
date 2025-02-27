import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?P<p>.?[a-z]){40}(?P<p>.?[a-z])', s[45:-3]))