from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    unique_palindromes.add(candidate)
    return unique_palindromes