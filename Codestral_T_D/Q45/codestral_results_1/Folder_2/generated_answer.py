import itertools

def palindromes_between_indices(s):
    s = s[1:6].lower()
    palindromes = set()
    for r in range(6, len(s) + 1):
        for perm in itertools.permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes