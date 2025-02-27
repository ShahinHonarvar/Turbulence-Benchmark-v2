from itertools import permutations

def palindromes_between_indices(s):
    if len(s) <= 7:
        return set()
    sub_string = s[3:8].lower()
    letters = ''.join(filter(str.isalpha, sub_string))
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindrome_set.add(perm_str)
    return palindrome_set