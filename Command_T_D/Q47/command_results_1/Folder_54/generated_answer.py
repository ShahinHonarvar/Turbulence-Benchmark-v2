import re

def palindromes_of_specific_lengths(str1):
    str1 = str1[27:77]
    pal = re.findall('[a-z]+', str1, flags=re.I)
    return set(pal)