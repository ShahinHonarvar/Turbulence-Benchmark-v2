from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[3:8].lower()
    english_letters = [char for char in substring if char.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            halfway = len(perm) // 2
            if perm[:halfway] == perm[-1:-(halfway + 1):-1]:
                unique_palindromes.add(''.join(perm))
    return unique_palindromes