from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[:6] if c.isalpha()]
    all_permutations = set((''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)))
    palindromes = {p for p in all_permutations if is_palindrome(p.lower())}
    return palindromes