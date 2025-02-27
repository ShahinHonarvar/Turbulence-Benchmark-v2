from itertools import permutations
    import re

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = re.findall('[a-z]', s)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes