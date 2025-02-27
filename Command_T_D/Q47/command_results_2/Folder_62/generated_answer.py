import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]{52,56}(?=\\W{26,87})[a-z]{52,56}', s.lower()))