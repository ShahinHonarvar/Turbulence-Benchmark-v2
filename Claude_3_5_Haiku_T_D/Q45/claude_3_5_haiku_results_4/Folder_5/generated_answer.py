from itertools import permutations

def palindromes_between_indices(s):
    subset = s[4:9]
    letters = [char.lower() for char in subset if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes