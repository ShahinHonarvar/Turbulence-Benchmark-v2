from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    segment = s[2:7].lower()
    letters = [char for char in segment if char.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes