from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substr = s[5:10].lower()
    letters = [ch for ch in substr if ch.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes