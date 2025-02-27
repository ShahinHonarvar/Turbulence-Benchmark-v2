import re
import string
from itertools import combinations

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[0:6])
    return {(four + two + two[::-1] + four[::-1]).lower() for four in combinations(letters, 4) for two in combinations(letters, 2)}