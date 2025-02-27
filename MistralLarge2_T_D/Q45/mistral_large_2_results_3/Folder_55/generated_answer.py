from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    chars = [c for c in s[:3] if c.isalpha()]
    if len(chars) < 3:
        return set()
    palindromes = set()
    for p in permutations(chars, 3):
        if is_palindrome(''.join(p)):
            palindromes.add(''.join(p))
    return palindromes