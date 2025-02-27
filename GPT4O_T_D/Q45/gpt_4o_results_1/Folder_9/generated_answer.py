from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    english_letters = [c for c in s if c.isalpha()]
    permutations_set = set([''.join(p) for p in permutations(english_letters)])
    palindromes = set()
    for p in permutations_set:
        if len(p) >= 7 and p == p[::-1]:
            palindromes.add(p)
    return palindromes