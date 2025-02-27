from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    substring = s[2:4].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        for length in range(3, len(perm_str) + 1):
            segment = perm_str[:length]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes