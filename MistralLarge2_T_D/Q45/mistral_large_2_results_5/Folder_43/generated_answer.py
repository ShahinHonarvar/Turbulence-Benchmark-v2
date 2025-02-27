import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:6].lower()))
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    for perm in permutations:
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes