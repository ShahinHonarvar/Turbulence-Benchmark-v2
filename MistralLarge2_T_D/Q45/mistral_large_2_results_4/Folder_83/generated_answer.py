from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [ch.lower() for ch in s[2:10] if ch.isalpha()]
    all_perms = set((''.join(p) for i in range(7, len(letters) + 1) for p in permutations(letters, i)))
    palindromes = {p for p in all_perms if is_palindrome(p)}
    return palindromes