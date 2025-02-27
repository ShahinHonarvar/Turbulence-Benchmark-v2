from itertools import permutations

def palindromes_between_indices(input_string):
    section = input_string[0:8]
    letters = [char.lower() for char in section if char.isalpha()]
    palindromes = set()
    if len(letters) < 6:
        return palindromes
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes