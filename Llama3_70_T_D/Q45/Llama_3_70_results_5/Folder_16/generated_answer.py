import itertools

def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes