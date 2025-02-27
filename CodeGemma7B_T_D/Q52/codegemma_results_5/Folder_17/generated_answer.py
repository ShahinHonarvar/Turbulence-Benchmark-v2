import re

def palindrome_of_length_n(s: str):
    pattern = re.compile('([a-zA-Z]{289})', flags=re.MULTILINE)
    return set(filter(str.casefold == str.casefold, pattern.findall(s)))