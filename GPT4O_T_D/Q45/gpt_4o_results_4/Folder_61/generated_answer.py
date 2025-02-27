from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[0:8]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for perm in set(permutations(s, len(s))):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and is_palindrome(perm_str):
            palindromes.add(perm_str)
    return palindromes