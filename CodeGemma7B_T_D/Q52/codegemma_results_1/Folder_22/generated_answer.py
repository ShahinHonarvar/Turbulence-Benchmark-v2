from itertools import product
import re

def palindrome_of_length_n(s):
    str_to_check = s.lower()
    return set([''.join(p) for p in product(str_to_check, repeat=20) if p == p[::-1] and re.match('^[a-zA-Z]+$', ''.join(p))])