import itertools

def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                if perm == perm[::-1]:
                    palindromes.add(''.join(perm))
    return palindromes