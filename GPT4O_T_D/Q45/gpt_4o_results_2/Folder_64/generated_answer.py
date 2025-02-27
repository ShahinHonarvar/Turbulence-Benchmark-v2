from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:10].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 5 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes