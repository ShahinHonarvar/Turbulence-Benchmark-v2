import re

def palindromes_between_indices(text):
    letters = re.findall('[A-Z]+', text)
    if not letters:
        return set()
    letters = ''.join(sorted(set(letters)))
    if len(letters) < 6:
        return set()
    return set(re.findall('((?=.)[A-Z]+)(\x01)[A-Z]+\x01', letters))