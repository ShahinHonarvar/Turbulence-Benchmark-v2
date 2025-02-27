from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[max(2, 0):min(8, len(s))]
    letters = [char.lower() for char in s if char.isalpha()]
    possible_permutations = set((''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)))
    palindromes = {word for word in possible_permutations if is_palindrome(word)}
    return palindromes