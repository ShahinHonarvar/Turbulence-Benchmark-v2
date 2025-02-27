from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string[3:8].lower()
    palindromes = set()
    for i in range(4, len(input_string) + 1):
        perms = set(permutations(input_string, i))
        for perm in perms:
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes