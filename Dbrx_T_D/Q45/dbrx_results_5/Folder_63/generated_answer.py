import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:4])
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            candidate = ''.join(letters[i:j + 1])
            if candidate == candidate[::-1]:
                palindromes.add(candidate.lower())
    return palindromes