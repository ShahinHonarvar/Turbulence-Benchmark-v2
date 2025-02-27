from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    target_section = s[1:8].lower()
    english_letters = [c for c in target_section if c.isalpha()]
    if len(english_letters) < 7:
        return set()
    palindromes_set = set()
    for perm in permutations(english_letters, 7):
        perm_word = ''.join(perm)
        if is_palindrome(perm_word):
            palindromes_set.add(perm_word)
    return palindromes_set