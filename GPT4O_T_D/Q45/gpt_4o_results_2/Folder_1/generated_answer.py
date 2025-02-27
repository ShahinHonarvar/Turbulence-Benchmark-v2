from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[4:8].lower()
    letters = [c for c in substring if c.isalpha()]
    if len(letters) < 5:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    letter_count = Counter(letters)
    possible_permutations = set(permutations(letters, 5))
    palindromes = {''.join(p) for p in possible_permutations if is_palindrome(''.join(p))}
    return palindromes