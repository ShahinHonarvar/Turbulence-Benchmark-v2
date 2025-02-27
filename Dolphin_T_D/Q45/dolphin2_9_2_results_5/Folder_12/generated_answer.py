import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for subset in itertools.combinations(letters, r):
            for perm in itertools.permutations(subset):
                word = ''.join(''.join(perm))
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes