import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[3:9] if c.isalpha()]
    permutations = set((''.join(p) for r in range(7, len(letters) + 1) for p in itertools.permutations(letters, r)))
    return {word for word in permutations if is_palindrome(word) and len(word) >= 7}