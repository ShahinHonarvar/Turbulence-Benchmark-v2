import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes