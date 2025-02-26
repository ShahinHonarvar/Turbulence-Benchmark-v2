from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:10] if char.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                if len(arrangement) % 2 == 0:
                    mid = len(arrangement) // 2
                    if arrangement[:mid] == arrangement[mid:][::-1]:
                        unique_palindromes.add(''.join(arrangement))
                else:
                    mid = len(arrangement) // 2
                    if arrangement[:mid] == arrangement[mid + 1:][::-1]:
                        unique_palindromes.add(''.join(arrangement))
    return unique_palindromes