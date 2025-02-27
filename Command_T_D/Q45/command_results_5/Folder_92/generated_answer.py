import re

def palindromes_between_indices(s):
    return set(re.findall('((?=([^aieou])\x01)[^aieou]*((?<=\x01)[^aieou])\x02\x02)', s[4:-7]))