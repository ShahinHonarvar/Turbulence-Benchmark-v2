from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[2:5].lower())
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in permutations(letters, 4):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes