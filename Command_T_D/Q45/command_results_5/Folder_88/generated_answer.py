import re

def palindromes_between_indices(s):
    return re.findall('(?i)(?=([^aieou]))([aieou])([aieou])([aieou])([aieou])([aieou])([aieou])', s)