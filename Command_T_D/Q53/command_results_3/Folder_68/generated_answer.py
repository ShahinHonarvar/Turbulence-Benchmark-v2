import re

def palindrome_of_length_at_least_n(s):
    if not s:
        return set()
    return set(re.findall('[a-z]+', s, flags=re.IGNORECASE))