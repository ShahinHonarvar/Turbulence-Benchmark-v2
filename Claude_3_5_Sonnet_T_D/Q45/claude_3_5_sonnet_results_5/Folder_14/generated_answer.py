from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = ''.join((char for char in s[4:6] if char.isalpha()))
    letters = letters.lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes