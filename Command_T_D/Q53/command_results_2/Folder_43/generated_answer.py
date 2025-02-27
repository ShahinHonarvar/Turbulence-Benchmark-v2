import re

def palindrome_of_length_at_least_n(test_str):
    pal_str = re.findall('[a-z]{50}', test_str.lower(), flags=re.I)
    return set(pal_str)