from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 6)):
        for p in [''.join(perm), ''.join(perm[::-1])]:
            if p == p[::-1] and len(set(p)) > 2:
                unique_palindromes.add(p)
    return unique_palindromes