from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                candidate = list(perm[i:j])
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes