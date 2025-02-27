import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[a-z]{30,300}(?=\\W|$)', text[3:-300]))