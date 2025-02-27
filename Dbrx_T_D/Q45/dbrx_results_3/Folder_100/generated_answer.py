from functools import reduce
import re

def palindromes_between_indices(s):
    chars = set(re.findall('[a-z]', s[:6].lower()))
    return {x for i in range(6, len(s) + 1) for x in itertools.product(chars, repeat=i) if x == x[::-1]}