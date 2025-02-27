from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    chars = [c for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
    return palindromes