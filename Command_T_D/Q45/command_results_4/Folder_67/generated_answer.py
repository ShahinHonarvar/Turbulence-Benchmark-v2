import re

def palindromes_between_indices(s):
    if not s:
        return set()
    return set(re.findall('(?i)(?<=.)([a-z])([a-z][a-z])([a-z][a-z][a-z])([a-z][a-z][a-z][a-z])([a-z][a-z][a-z][a-z][a-z])', s))