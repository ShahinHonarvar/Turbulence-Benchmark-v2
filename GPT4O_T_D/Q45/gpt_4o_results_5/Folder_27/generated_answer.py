from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[2:9].lower()
    letters = [c for c in s if c.isalpha()]
    possible_palindromes = set()
    if len(letters) < 6:
        return set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 6 and is_palindrome(word):
            possible_palindromes.add(word)
    return possible_palindromes