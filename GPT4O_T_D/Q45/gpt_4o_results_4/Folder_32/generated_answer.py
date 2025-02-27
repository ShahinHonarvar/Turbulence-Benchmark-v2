from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    selected_part = s[1:8].lower()
    english_letters = ''.join(filter(str.isalpha, selected_part))
    valid_palindromes = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and is_palindrome(perm_str):
            valid_palindromes.add(perm_str)
    return valid_palindromes