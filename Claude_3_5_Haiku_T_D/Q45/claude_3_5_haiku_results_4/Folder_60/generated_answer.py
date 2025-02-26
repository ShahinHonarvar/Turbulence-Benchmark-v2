from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        candidate = ''.join(perm)
        if len(set(candidate)) >= 4:
            for p in [candidate + candidate[::-1], candidate[::-1] + candidate]:
                if p == p[::-1] and len(p) >= 4:
                    palindromes.add(p)
    return palindromes