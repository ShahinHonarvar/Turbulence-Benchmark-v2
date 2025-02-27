import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha() and c.isascii()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for subset in itertools.combinations(letters, r):
            for arrangement in itertools.permutations(subset):
                word = ''.join(arrangement)
                if word == word.lower():
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes