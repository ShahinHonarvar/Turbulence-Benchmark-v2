import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [ch for ch in s[1:7] if ch.isalpha()]
    permutations = set((''.join(p) for i in range(6, len(letters) + 1) for p in itertools.permutations(letters, i)))
    palindromes = {p for p in permutations if is_palindrome(p)}
    return palindromes