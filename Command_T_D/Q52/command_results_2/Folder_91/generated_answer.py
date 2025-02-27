import re

def palindrome_of_length_n(s):
    if len(s) < 7:
        return set()
    return set(re.findall('[a-z]{7}'.lower(), s))