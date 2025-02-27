from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[5:10] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word) and len(word) >= 6:
                palindromes.add(word.lower())
    return palindromes