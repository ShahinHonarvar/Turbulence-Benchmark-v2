from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:6].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_word = ''.join(perm)
            if is_palindrome(perm_word):
                palindromes.add(perm_word)
    return palindromes