import re

def palindromes_between_indices(str):
    return set(re.findall('[a-z]{5,}(?=([a-z]{2}(?=([a-z]{4}(?=[a-z]))))', str))