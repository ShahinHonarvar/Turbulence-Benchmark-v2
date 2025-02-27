from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]
    unique_permutations = set(permutations(letters))
    palindromes = set()
    for perm in unique_permutations:
        for i in range(3, len(letters) + 1):
            sub_perm = perm[:i]
            if sub_perm == sub_perm[::-1]:
                palindromes.add(''.join(sub_perm))
    return {p for p in palindromes if len(p) >= 4}