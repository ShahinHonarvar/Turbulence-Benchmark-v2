import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[4:10])
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in set(itertools.permutations(letters, i)):
            if str(perm) == str(perm)[::-1]:
                palindromes.add(''.join(perm).lower())
    return palindromes