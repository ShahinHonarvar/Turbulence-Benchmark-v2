import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=([^aieou]))([aieou])([aieou])([aieou])([aieou])([aieou])', s[2:-6:-1]))