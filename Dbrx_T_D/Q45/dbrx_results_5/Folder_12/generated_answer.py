import re
from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[3:9])
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for i in range(4, len(english_letters) + 1):
        d = defaultdict(list)
        for j in range(len(english_letters) - i + 1):
            d[''.join(sorted(english_letters[j:j + i]))].append(''.join(english_letters[j:j + i]))
        for k in d.values():
            if len(k) > 1:
                palindromes.update(k)
    return {p.lower() for p in palindromes}