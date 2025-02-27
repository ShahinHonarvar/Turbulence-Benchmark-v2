from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[2:6].lower())
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters, 5):
        if is_palindrome(''.join(perm)):
            palindromes.add(''.join(perm))
    return palindromes