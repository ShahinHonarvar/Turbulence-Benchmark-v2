from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[8:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                arrangement_str = ''.join(arrangement)
                if arrangement_str == arrangement_str[::-1]:
                    palindromes.add(arrangement_str)
    return palindromes