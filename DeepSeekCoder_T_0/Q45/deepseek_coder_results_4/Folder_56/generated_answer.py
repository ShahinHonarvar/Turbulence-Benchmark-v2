from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:10])).lower()
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        if is_palindrome(''.join(perm)) and len(''.join(perm)) >= 5:
            palindromes.add(''.join(perm))
    return palindromes