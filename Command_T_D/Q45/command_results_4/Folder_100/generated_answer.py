import re

def palindromes_between_indices(text):
    return set(re.findall('(?=([a-z]+){6})[a-z]+', text.lower()))