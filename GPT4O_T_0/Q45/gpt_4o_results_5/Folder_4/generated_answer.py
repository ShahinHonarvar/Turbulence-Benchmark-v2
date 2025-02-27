from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        if len(perm) >= 7:
            for i in range(len(perm) - 6):
                sub_perm = perm[i:i + 7]
                if sub_perm == sub_perm[::-1]:
                    palindromes.add(''.join(sub_perm))
    return palindromes