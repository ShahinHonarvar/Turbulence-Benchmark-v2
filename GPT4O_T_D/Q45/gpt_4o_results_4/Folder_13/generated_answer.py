from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:10].lower()
    letters = [c for c in sub_str if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        candidate = ''.join(perm)
        if len(candidate) >= 5 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes