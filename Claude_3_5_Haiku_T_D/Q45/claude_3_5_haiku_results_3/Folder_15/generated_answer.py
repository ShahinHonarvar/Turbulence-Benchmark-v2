from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                candidate = ''.join(perm[i:j])
                if len(candidate) >= 3 and candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes