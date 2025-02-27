import re

def palindromes_between_indices(s):
    return set(re.findall('((?=.)(?P<palidrome>[a-z]){6}(?=.)\x02)', s[2:-2]))