from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:8] if char.isalpha()]
    result = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result