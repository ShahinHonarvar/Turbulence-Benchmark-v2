from itertools import permutations

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[1:7] if c.isalpha()])
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            s = ''.join(p)
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes