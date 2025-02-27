from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:10])).lower()
    if len(letters) < 4:
        return set()
    all_perms = set((''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)))
    palindromes = {p for p in all_perms if is_palindrome(p) and len(p) >= 4}
    return palindromes