import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[0:8])
    if len(letters) < 6:
        return set()
    letters = [x.lower() for x in letters]
    result = set()
    for i in range(len(letters) - 5):
        for j in range(i, len(letters) - i):
            if letters[i:j + 1] == letters[i:j + 1][::-1]:
                result.add(''.join(letters[i:j + 1]))
    return result