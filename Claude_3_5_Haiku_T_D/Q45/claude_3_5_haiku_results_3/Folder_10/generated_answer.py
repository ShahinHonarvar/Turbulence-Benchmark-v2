from itertools import permutations

def palindromes_between_indices(s):
    subset = s[0:6].lower()
    letter_subset = [char for char in subset if char.isalpha()]
    unique_palindromes = set()
    for length in range(3, len(letter_subset) + 1):
        for perm in set(permutations(letter_subset, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1] and len(candidate) >= 3:
                    unique_palindromes.add(candidate)
    return unique_palindromes