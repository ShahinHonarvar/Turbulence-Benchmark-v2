from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    sub_str = s[7:10].lower()
    letters = [char for char in sub_str if char.isalpha()]
    if len(letters) < 4:
        return set()
    possible_palindromes = set()
    for perm in permutations(letters, len(letters)):
        half_length = len(perm) // 2
        if list(perm[:half_length]) == list(reversed(perm[-half_length:])):
            possible_palindromes.add(''.join(perm))
    return {p for p in possible_palindromes if len(p) >= 4}