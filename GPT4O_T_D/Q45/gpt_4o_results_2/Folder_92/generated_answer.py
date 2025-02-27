from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    sub_string = s[4:8].lower()
    letters = [c for c in sub_string if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes