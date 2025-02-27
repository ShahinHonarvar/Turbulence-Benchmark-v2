import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    chars = defaultdict(int)
    for c in s[0:6]:
        chars[c] += 1
    palindromes = set()
    for i in range(5, 0, -1):
        for combo in itertools.combinations_with_replacement(chars.keys(), i):
            if len(combo) == 1:
                if chars[combo[0]] >= 2:
                    palindromes.add(combo[0] * i)
                continue
            candidate = ''.join(combo)
            if candidate == candidate[::-1] and s[0:6].count(candidate) == i:
                palindromes.add(candidate)
    return palindromes