from itertools import combinations

def palindromes_between_indices(s):
    letters = [c for c in s.lower() if c.isalpha()]
    length = len(letters)
    if length < 7:
        return set()
    palindromes = set()
    for i in range(7, length + 1):
        for comb in combinations(letters, i):
            for p in range(i):
                r = i - p - 1
                if all((comb[p] == comb[r] for p in range(i))):
                    palindromes.add(''.join(comb))
    return palindromes