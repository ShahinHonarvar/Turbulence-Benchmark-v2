from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = s[3:7].lower()
    chars = [char for char in subset if char.isalpha()]
    palindromes = set()
    for perm in permutations(chars):
        permuted_word = ''.join(perm)
        if len(permuted_word) >= 4 and is_palindrome(permuted_word):
            palindromes.add(permuted_word)
    return palindromes