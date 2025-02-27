from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = ''.join([c.lower() for c in s[2:5] if c.isalpha()])
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in permutations(substr, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes