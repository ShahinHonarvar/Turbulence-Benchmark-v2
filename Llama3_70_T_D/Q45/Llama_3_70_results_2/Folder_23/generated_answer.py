import itertools

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes