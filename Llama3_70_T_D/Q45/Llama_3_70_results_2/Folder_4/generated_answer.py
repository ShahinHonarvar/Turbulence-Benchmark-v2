import itertools

def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(7, len(s) + 1):
        for combination in itertools.combinations(s, r):
            for arrangement in itertools.permutations(combination):
                word = ''.join(arrangement)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes