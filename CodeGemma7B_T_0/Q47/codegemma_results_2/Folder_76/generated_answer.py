import re

def palindromes_of_specific_lengths(text):
    pattern = '(?i)(?:(?<=\\\\s|^)[a-z]{154,182}(?=\\\\s|$))|(?i)(?:(?<=\\\\s|^)[a-z]{154,182}(?=\\\\s|$))'
    return set(re.findall(pattern, text))