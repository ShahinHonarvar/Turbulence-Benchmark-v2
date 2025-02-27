import re
    from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    letters = re.findall('[a-z]', s[:7])
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for start in range(len(letters) - length + 1):
            current = letters[start:start + length]
            if current == current[::-1]:
                palindromes.add(''.join(current))
    return palindromes