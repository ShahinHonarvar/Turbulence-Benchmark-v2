from itertools import permutations

def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(1, 5) if s[i].isalpha()))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes