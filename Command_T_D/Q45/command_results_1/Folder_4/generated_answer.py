import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=([^aieou]))[aieou]{7}(?=[^aieou]*$)', s[3:-9]))