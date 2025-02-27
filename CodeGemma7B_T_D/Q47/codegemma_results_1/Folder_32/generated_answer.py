import re

def palindromes_of_specific_lengths(string):
    matches = re.findall('(?i)\\\\b[A-Za-z]{43,47}\\\\b', string[16:78])
    return set(matches)