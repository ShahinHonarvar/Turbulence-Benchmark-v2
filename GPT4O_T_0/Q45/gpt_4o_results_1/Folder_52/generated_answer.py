from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        for length in range(6, len(perm) + 1):
            for i in range(len(perm) - length + 1):
                sub_perm = perm[i:i + length]
                if sub_perm == sub_perm[::-1]:
                    palindromes.add(''.join(sub_perm))
    return palindromes