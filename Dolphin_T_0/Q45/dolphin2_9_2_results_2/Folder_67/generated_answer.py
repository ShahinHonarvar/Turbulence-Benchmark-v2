import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for subset in itertools.combinations(letters, r):
            for p in itertools.permutations(subset, r):
                word = ''.join(p)
                if word == word[::-1] and word.islower():
                    palindromes.add(word)
    return palindromes