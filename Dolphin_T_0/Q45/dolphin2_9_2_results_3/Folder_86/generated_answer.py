import itertools

def palindromes_between_indices(s):
    palindromes = set()
    for p in itertools.permutations(s[6:10], len(s[6:10]) - 6 + 1):
        for i in range(len(p)):
            if p[i:i + 4] == p[i:i + 4][::-1]:
                palindromes.add(p[i:i + 4])
    return palindromes