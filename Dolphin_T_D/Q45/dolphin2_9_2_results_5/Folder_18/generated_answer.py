import itertools
    from sets import Set

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = Set()
    for r in range(3, len(letters) + 1):
        combinations = list(itertools.combinations(letters, r))
        for c in combinations:
            for p in itertools.permutations(c):
                word = ''.join(p)
                if word == word[::-1]:
                    palindromes.add(word.lower())
    return palindromes