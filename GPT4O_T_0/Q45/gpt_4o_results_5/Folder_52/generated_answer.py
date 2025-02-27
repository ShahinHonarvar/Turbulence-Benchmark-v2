from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        for length in range(6, len(perm) + 1):
            for i in range(len(perm) - length + 1):
                sub = perm[i:i + length]
                if sub == sub[::-1]:
                    palindromes.add(''.join(sub))
    return palindromes