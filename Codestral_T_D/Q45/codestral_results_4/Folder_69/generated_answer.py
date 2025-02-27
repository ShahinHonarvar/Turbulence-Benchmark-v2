import itertools

def palindromes_between_indices(s):
    s = s[0:4].lower()
    palindromes = set()
    for perm in itertools.permutations(s):
        for i in range(len(perm)):
            for j in range(i + 4, len(perm) + 1):
                substring = perm[i:j]
                if substring == substring[::-1]:
                    palindromes.add(''.join(substring))
    return palindromes