import re
    from itertools import permutations

def palindromes_between_indices(s):
    substr = re.sub('[^a-zA-Z]', '', s[:5]).lower()
    letters = set(substr)
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for p in permutations(substr, length):
            if ''.join(p) == ''.join(p)[::-1]:
                palindromes.add(''.join(p))
    return palindromes