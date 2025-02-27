from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if is_palindrome(word) and len(word) >= 5:
            palindromes.add(word)
    return palindromes