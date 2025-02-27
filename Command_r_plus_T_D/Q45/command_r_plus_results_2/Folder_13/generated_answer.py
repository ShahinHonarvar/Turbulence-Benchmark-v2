import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:10])
    if not letters:
        return set()
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in set(itertools.permutations(letters, i)):
            word = ''.join(perm).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes