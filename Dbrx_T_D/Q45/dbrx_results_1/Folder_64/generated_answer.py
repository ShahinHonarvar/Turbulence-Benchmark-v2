import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[4:10])
    if len(letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            subset = letters[i:i + length]
            if subset == subset[::-1]:
                palindromes.add(''.join(subset).lower())
    return palindromes