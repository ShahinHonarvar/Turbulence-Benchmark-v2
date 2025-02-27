from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub_range = s[2:6]
    letters = [char.lower() for char in sub_range if char.isalpha()]
    potential_palindromes = set()
    for word_permutation in permutations(letters):
        word = ''.join(word_permutation)
        if len(word) >= 5 and is_palindrome(word):
            potential_palindromes.add(word)
    return potential_palindromes