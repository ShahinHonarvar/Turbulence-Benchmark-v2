import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for arrangement in itertools.permutations(combo):
                word = ''.join(arrangement)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes