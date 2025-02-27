import itertools

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes