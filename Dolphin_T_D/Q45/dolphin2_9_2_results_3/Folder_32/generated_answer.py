import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[1:8] if ch.isalpha()]
    palindromes = set()
    for p in range(5, len(letters) + 1):
        for subset in itertools.combinations(letters, p):
            for perm in itertools.permutations(subset):
                word = ''.join(perm)
                if word.lower() == word[::-1].lower():
                    palindromes.add(word)
    return palindromes