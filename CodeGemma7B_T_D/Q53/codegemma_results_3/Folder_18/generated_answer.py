import re

def palindrome_of_length_at_least_n(text):
    pattern = '[a-zA-Z]{62,}'
    matches = re.findall(pattern, text.lower())
    '\n            The below code is checking if the matches contains atleast one element.\n            Return the unique palindromes in a set.\n            '
    if len(matches) > 0:
        return set(matches)
    else:
        return set()