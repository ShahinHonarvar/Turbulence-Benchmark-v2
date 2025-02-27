from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[7:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes