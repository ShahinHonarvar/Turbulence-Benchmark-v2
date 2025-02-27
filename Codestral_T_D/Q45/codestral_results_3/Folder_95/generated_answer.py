import itertools

def palindromes_between_indices(string):
    letters = string[7:9]
    letters = letters.lower()
    permutations = itertools.permutations(letters)
    palindromes = set()
    for perm in permutations:
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 3:
            palindromes.add(perm_str)
    return palindromes