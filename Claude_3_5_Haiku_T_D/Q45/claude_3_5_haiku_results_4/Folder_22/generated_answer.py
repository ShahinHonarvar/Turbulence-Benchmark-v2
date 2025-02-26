from itertools import permutations

def palindromes_between_indices(s):
    subset = s[5:7]
    letters = [char.lower() for char in subset if char.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = list(arrangement)
                if candidate == candidate[::-1]:
                    unique_palindromes.add(''.join(candidate))
    return unique_palindromes