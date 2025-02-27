from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[3:10].lower()
    s = ''.join(filter(str.isalpha, s))
    found_palindromes = set()
    if len(s) < 7:
        return found_palindromes
    for perm in permutations(s, len(s)):
        word = ''.join(perm)
        if len(word) >= 7 and is_palindrome(word):
            found_palindromes.add(word)
    return found_palindromes