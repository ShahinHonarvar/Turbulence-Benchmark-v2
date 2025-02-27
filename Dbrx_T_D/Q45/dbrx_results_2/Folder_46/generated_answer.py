from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[4:10].lower()))).replace('{', '').replace('}', '')
    palindromes = set()
    if len(letters) >= 6:
        for perm in permutations(letters, 6):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes