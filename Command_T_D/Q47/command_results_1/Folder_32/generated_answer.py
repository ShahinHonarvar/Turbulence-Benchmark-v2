import re

def palindromes_of_specific_lengths(test_str):
    return re.findall('[a-z]{43,47}', test_str[16:77])