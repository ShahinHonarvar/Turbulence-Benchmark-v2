import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[4:10])).lower()
    if len(s) < 5:
        return set()
    letters = sorted(s)
    palindromes = set()
    for r in range(5, len(s) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes