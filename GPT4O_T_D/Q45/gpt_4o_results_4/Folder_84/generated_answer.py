from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letters = [c for c in substring if c.isalpha()]
    if len(letters) < 3:
        return set()
    possible_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            half_length = length // 2
            if perm[:half_length] == perm[-half_length:][::-1]:
                possible_palindromes.add(''.join(perm))
    return possible_palindromes