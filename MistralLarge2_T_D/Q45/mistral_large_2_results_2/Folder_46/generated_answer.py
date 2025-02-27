from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:10]
    english_letters = [c.lower() for c in substring if c.isalpha()]
    all_permutations = set((''.join(p) for i in range(6, len(english_letters) + 1) for p in permutations(english_letters, i)))
    palindromes = {p for p in all_permutations if is_palindrome(p) and len(p) >= 6}
    return palindromes