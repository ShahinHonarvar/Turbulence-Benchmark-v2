from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    if len(s) < 10:
        return palindromes
    sub_str = s[5:10]
    letters = [char.lower() for char in sub_str if char.isalpha()]
    if len(letters) < 5:
        return palindromes
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes