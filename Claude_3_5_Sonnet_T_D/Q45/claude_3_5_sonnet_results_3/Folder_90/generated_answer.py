from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes