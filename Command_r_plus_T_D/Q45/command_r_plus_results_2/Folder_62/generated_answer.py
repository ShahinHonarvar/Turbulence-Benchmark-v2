import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:9])
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in set(itertools.permutations(letters, i)):
            if str(perm) == str(perm)[::-1]:
                palindromes.add(''.join(perm).lower())
    return palindromes