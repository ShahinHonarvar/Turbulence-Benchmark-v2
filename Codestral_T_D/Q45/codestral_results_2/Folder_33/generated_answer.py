import itertools

def palindromes_between_indices(s):
    s = s[7:10].lower()
    palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in itertools.permutations(s, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes