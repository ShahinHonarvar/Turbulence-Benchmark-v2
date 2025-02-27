from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for i in range(5, 2, -1):
        for perm in permutations(s, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes