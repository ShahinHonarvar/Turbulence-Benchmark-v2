import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[1:7])).lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for combo in itertools.combinations(s, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes