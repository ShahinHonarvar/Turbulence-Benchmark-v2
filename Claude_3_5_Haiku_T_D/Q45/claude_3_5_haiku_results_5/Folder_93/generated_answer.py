from itertools import permutations

def palindromes_between_indices(s):
    letters_in_range = [char.lower() for char in s[2:8] if char.isalpha()]
    palindromes = set()
    for length in range(6, len(letters_in_range) + 1):
        for perm in set(permutations(letters_in_range, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes