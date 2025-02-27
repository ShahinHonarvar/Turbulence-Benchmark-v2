import re

def palindromes_of_specific_lengths(s):
    return re.findall('(?i)(?=([A-Z][A-Z] [A-Z]))( [A-Z][A-Z] [A-Z])', s[100:300])