from itertools import permutations

def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    sub_str = s[5:9]
    english_letters = get_english_letters(sub_str)
    all_permutations = permutations(english_letters)
    palindromes = set((perm for perm in all_permutations if len(perm) >= 3 and is_palindrome(''.join(perm))))
    return palindromes