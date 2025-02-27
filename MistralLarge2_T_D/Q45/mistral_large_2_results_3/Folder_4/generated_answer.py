from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars_between_indices = [c for c in s[3:10] if c.isalpha()]
    lower_chars = [c.lower() for c in chars_between_indices]
    palindromes = set()
    for length in range(7, len(lower_chars) + 1):
        for perm in permutations(lower_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes