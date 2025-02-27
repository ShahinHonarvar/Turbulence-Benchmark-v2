import re

def palindromes_between_indices(s):
    return set(re.findall('((?=.)\\d+)(?=.)(?!\\d)(\\d+)(?!\\d)(?=.)\\d+)(?=.)\\d+)(?!\\d)', s[0:6:2]))