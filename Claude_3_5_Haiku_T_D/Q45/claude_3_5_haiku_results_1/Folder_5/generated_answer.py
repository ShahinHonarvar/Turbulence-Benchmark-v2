from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    section = s[4:9]
    letters = ''.join((char.lower() for char in section if char.isalpha()))
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters, len(letters))):
        test_str = ''.join(perm)
        if len(test_str) >= 4 and test_str == test_str[::-1]:
            palindrome_set.add(test_str)
    return palindrome_set