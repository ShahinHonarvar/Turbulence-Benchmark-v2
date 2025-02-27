from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    english_letters = ''.join([c for c in s[0:7] if c.isalpha()])
    palindromes = set()
    if len(english_letters) < 7:
        return set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and is_palindrome(perm_str):
            palindromes.add(perm_str)
    return palindromes