from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substr = s[2:7].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                if len(arrangement) >= 4:
                    candidate = ''.join(arrangement)
                    rev_candidate = candidate[::-1]
                    if candidate == rev_candidate:
                        palindromes.add(candidate)
    return palindromes