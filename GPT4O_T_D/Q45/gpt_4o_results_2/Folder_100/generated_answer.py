from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:6].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in permutations(letters, 6):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes