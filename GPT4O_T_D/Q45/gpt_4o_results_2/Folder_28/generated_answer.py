from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[1:6].lower()
    letters = ''.join(filter(str.isalpha, sub_str))
    palindromes = set()
    for n in range(4, len(letters) + 1):
        for perm in permutations(letters, n):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes