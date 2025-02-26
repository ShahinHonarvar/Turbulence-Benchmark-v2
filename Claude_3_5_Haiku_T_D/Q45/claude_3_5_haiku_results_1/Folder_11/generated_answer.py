from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(4, len(perm) + 1):
            for combo in set(permutations(perm, length)):
                candidate = ''.join(combo)
                if candidate == candidate[::-1] and len(candidate) >= 4:
                    palindromes.add(candidate)
    return palindromes