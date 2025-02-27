import itertools

def palindromes_between_indices(s):
    s = s[1:4].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for perm in itertools.permutations(s, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes