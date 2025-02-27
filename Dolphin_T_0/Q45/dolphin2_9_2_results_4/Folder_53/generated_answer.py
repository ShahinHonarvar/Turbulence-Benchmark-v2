import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[4:9] if ch.isalpha()]
    palindromes = set()
    for p in range(6, len(letters) + 1):
        for subset in itertools.combinations(letters, p):
            for permutation in itertools.permutations(subset):
                word = ''.join(permutation).lower()
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes