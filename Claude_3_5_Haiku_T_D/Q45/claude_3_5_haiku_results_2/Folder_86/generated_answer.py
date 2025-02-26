from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[6:10] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for p in set(permutations(perm)):
                candidate = ''.join(p).lower()
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes