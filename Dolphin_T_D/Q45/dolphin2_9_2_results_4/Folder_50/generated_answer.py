import itertools

def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[4:9] if c.isalpha()]))
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for subset in itertools.combinations(letters, length):
            for perm in itertools.permutations(subset):
                word = ''.join(perm)
                if word == word.lower() or word == word.upper():
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes