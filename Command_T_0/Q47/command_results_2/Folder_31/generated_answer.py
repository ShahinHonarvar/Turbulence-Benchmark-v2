import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('(?i)(?=([a-z]+){37,60}(?i)([a-z]+){37,60})', s[11:-11]))