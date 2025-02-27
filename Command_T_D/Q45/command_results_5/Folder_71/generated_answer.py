import re

def palindromes_between_indices(s):
    return set(re.findall('(?=.)\\w{3}|(?<=.)\\w{3}\\w{2}\\w{2}\\w{3}', s))