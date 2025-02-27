import re

def palindromes_of_specific_lengths(text):
    pattern = '[A-Za-z]{103,158}$'
    regex_result = re.findall(pattern, text[130:296])
    return set(regex_result)