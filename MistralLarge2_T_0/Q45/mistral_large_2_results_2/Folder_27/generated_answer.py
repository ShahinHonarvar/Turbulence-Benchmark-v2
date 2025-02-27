from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[2:9] if c.isalpha()]
    letters_lower = [c.lower() for c in letters]
    palindromes = set()
    for length in range(6, len(letters_lower) + 1):
        for perm in permutations(letters_lower, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes