import itertools

def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1] and len(word) >= 4:
                    palindromes.add(word)
    return palindromes