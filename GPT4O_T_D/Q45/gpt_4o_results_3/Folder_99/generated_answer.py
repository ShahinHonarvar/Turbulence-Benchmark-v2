from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:9].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    seen = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str not in seen:
            if len(perm_str) >= 3 and is_palindrome(perm_str):
                palindromes.add(perm_str)
            seen.add(perm_str)
    return palindromes