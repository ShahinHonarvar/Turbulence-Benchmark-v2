from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for perm in permutations(text[1:8], 4):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes