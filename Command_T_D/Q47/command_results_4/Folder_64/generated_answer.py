import re

def palindromes_of_specific_lengths(str):
    return re.findall('<(.)(.)(.)(.)(.)(.)(.)>(?=.)', str, flags=re.I)