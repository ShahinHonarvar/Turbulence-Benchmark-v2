from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    if len(s) < 7:
        return set()
    substring = s[3:7].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes