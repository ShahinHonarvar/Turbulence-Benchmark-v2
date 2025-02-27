from itertools import permutations

def palindromes_between_indices(input_string):
    if len(input_string) < 10:
        return set()
    substring = input_string[8:10]
    letters = [c.lower() for c in substring if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes