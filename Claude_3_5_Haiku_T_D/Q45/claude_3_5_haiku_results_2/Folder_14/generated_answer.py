from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:6] if char.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                test_str = ''.join(arrangement)
                if test_str == test_str[::-1] and len(test_str) >= 3:
                    unique_palindromes.add(test_str)
    return unique_palindromes