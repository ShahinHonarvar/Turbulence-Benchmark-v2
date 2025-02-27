import re

def palindromes_between_indices(s):
    return set(re.findall('<(?P<s>.{5,})>(?P=s)>', s))