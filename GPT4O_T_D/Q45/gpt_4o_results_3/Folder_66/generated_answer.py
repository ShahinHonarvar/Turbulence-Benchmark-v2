from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:6].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(s, len(s)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and is_palindrome(perm_str):
            palindromes.add(perm_str)
    return palindromes