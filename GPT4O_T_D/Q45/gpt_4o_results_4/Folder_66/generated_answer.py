from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:6].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    all_permutations = set((''.join(p) for p in permutations(english_letters)))
    palindromes_set = {perm for perm in all_permutations if len(perm) >= 5 and is_palindrome(perm)}
    return palindromes_set