import math
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    substring = s[2:6]
    palindromes = set()
    for i in range(len(substring)):
        for p in permutations(substring, i + 3):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes