import itertools

def palindromes_between_indices(s):
    s = s[7:9].lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations(s, r):
            for perm in itertools.permutations(combo):
                if perm == perm[::-1]:
                    palindromes.add(''.join(perm))
    return palindromes