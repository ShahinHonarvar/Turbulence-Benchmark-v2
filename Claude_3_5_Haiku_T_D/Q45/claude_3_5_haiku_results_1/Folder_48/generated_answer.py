from itertools import permutations

def palindromes_between_indices(s):
    letters_range = s[6:9]
    valid_letters = [char.lower() for char in letters_range if char.isalpha()]
    if len(valid_letters) < 4:
        return set()
    palindromes = set()
    for r in range(4, len(valid_letters) + 1):
        for perm in set(permutations(valid_letters, r)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1] and len(candidate) >= 4:
                    palindromes.add(candidate)
    return palindromes