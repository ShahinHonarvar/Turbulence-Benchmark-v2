import itertools

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[0:7].lower())))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, i):
            for p in itertools.permutations(combo):
                word = ''.join(p)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes