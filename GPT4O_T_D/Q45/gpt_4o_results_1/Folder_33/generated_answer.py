from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    segment = s[7:10].lower()
    letters = [char for char in segment if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes