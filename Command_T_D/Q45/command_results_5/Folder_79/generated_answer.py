import re

def palindromes_between_indices(s):
    m = re.findall('(?P<A>.{8})(?P<B>.{8})(?P=A)', s.lower())
    return set(m)