from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in combinations(letters, length // 2):
            if length % 2 == 0:
                p = ''.join(combo + combo[::-1])
            else:
                p = ''.join(combo + letters[length // 2 % len(letters)] + combo[::-1])
            for perm in permutations(p):
                palindromes.add(''.join(perm))
    return palindromes