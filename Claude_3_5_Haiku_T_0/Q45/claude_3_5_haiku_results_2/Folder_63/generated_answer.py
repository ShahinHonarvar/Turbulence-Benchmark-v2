from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:4] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes