from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 5 and is_palindrome(word):
            palindromes.add(word)
    return palindromes