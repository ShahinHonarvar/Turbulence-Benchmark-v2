from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:9] if c.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                candidate = ''.join(perm[i:j] + perm[i:j][::-1])
                if len(candidate) >= 3 and candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes