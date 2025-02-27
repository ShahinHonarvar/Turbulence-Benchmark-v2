import re

def palindromes_between_indices(text):
    return set(re.findall('[a-z]{5,}'.lower(), text[4:-2].lower()))