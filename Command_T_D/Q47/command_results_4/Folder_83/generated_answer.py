import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('(?i)(?<=\\d75)\\w{7}\\w{7}(?=\\d95)', text))