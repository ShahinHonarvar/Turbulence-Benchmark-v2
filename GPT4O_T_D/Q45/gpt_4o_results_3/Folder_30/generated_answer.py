from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = s[0:5].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes