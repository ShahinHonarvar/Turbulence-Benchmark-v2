import re

def palindromes_between_indices(s):
    letters = ''.join((c for c in s if c.isalpha()))
    if not letters:
        return set()
    length = len(letters) // 2
    return set(re.findall('((?:[a-z]){,5})\x01', letters[0:length]))