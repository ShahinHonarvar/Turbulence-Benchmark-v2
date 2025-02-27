from itertools import permutations

def palindromes_between_indices(s):
    from_index = 0
    to_index = 4
    substring = ''.join(filter(str.isalpha, s[from_index:to_index + 1].lower()))
    palindromes = set()
    if len(substring) < 2:
        return palindromes
    for length in range(4, len(substring) + 1):
        for perm in set(permutations(substring, length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes