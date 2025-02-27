from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 7):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes