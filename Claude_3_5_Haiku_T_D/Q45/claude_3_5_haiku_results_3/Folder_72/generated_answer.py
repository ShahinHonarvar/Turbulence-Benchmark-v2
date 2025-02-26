from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for p in set(permutations(perm)):
                candidate = ''.join(p)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes