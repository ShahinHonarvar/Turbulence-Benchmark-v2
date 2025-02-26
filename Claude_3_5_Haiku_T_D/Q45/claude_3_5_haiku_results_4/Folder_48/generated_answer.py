from itertools import permutations

def palindromes_between_indices(s):
    letters_in_range = [c.lower() for c in s[6:9] if c.isalpha()]
    if len(letters_in_range) < 4:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters_in_range, 4)):
        for length in range(4, len(perm) + 1):
            for combo in set(permutations(perm, length)):
                candidate = ''.join(combo)
                if candidate == candidate[::-1]:
                    unique_palindromes.add(candidate)
    return unique_palindromes