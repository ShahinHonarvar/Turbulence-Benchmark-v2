import itertools

def palindromes_between_indices(s):
    palindromes = set()
    for p in range(3, 9):
        for i in itertools.permutations(s[3:p], len(s[3:p])):
            t = ''.join(i)
            if len(t) >= 7 and t.lower() == t.lower()[::-1]:
                palindromes.add(t)
    return palindromes