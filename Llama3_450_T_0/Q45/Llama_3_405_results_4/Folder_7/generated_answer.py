import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:10].lower() if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1] and set(p) <= letters_set:
                    palindromes.add(p)
    return palindromes