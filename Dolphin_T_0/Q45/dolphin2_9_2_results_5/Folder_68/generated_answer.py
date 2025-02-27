import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[1:9] if ch.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for subset in itertools.combinations(letters, r):
            for permutation in itertools.permutations(subset):
                word = ''.join(permutation)
                if word == word[::-1]:
                    palindromes.add(word.lower())
    return palindromes