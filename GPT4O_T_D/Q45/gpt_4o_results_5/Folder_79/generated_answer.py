from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[1:8].lower()
    filtered_string = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for length in range(3, len(filtered_string) + 1):
        for perm in set(permutations(filtered_string, length)):
            perm_string = ''.join(perm)
            if perm_string == perm_string[::-1]:
                palindromes.add(perm_string)
    return palindromes