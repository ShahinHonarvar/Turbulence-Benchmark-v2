import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = [set(re.findall(f'(?i)[a-z]{{1}}', s[i])) - set() for i in range(4)]
    result = set()
    for i in range(4):
        for j in range(i, 8 - i):
            pal = ''.join(letters[i] & letters[j])
            if len(pal) >= 6:
                result.add(pal)
    return result