import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    permutations = itertools.permutations(letters, 7)
    palindromes = {''.join(p) for p in permutations if is_palindrome(''.join(p))}
    return palindromes