from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(phrase):
        return phrase == phrase[::-1]
    if len(s) < 10:
        return set()
    substring = s[6:10].lower()
    english_letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for i in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, i):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes